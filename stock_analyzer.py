import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def calculate_risk(prices):
    daily_returns = []

    for i in range(1, len(prices)):
        previous_price = prices[i - 1]
        current_price = prices[i]

        daily_return = ((current_price - previous_price) / previous_price) * 100
        daily_returns.append(daily_return)

    average_daily_return = sum(daily_returns) / len(daily_returns)

    squared_differences = []

    for daily_return in daily_returns:
        difference = daily_return - average_daily_return
        squared_difference = difference ** 2
        squared_differences.append(squared_difference)

    variance = sum(squared_differences) / (len(squared_differences) - 1)
    volatility = variance ** 0.5
    annualized_volatility = volatility * (252 ** 0.5)

    if annualized_volatility < 20:
        risk_level = "Low Risk"
    elif annualized_volatility <= 40:
        risk_level = "Medium Risk"
    else:
        risk_level = "High Risk"

    return annualized_volatility, risk_level, daily_returns

print("Stock Return Analyzer")

while True:
    try:
        number_of_stocks = int(input("How many stocks do you want to analyze? "))

        if number_of_stocks < 2:
            print("Please enter at least 2 stocks")
            continue

        break

    except ValueError:
        print("Please enter a whole number")

results = []

for i in range(number_of_stocks):
    print("Stock", i + 1)

    stock = input("Enter stock name: ")
    ticker = input("Please enter stock ticker: ").upper()

    file_name = ticker + ".csv"

    try:
        history = pd.read_csv(file_name)

    except FileNotFoundError:
        print("CSV file not found:", file_name)
        continue
    
    try:
        history["Date"] = pd.to_datetime(history["Date"])

        history["Close/Last"] = history["Close/Last"].str.replace("$", "", regex=False)
        history["Close/Last"] = history["Close/Last"].astype(float)

        history = history.sort_values("Date")

        prices = history["Close/Last"].tolist()

    except KeyError:
        print("Required column not found")
        continue
    
    if len(prices) < 3:
        print("Not enough price data")
        continue

    annualized_volatility, risk_level, daily_returns = calculate_risk(prices)

    return_series = pd.Series(
        daily_returns,
        index=history["Date"].iloc[1:]
    )

    plt.figure()
    plt.plot(history["Date"],history["Close/Last"])
    plt.title(stock + " Price History")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return_dates = history["Date"].tolist()[1:]

    plt.figure()
    plt.bar(return_dates, daily_returns)
    plt.axhline(0)
    plt.title(stock + " Daily Returns")
    plt.xlabel("Date")
    plt.ylabel("Daily Return (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    while True:
        try:
            buy_price = float(input("Enter buy price: "))

            if buy_price <= 0:
                print("Invalid buy price")
                continue

            break

        except ValueError:
            print("Please enter a number")
    
    current_price = prices[-1]
    print("Current Price:", current_price)
    
    while True:
        try:
            investment = float(input("Enter investment amount: "))

            if investment <= 0:
                print("Invalid investment amount")
                continue

            break

        except ValueError:
            print("Please enter a number")
    
    stock_return = ((current_price - buy_price) / buy_price) * 100
    profit_loss = investment * stock_return / 100
    current_value = investment + profit_loss

    if stock_return > 0:
        status = "Profit"
    elif stock_return < 0:
        status = "Loss"
    else:
        status = "Break Even"
    
    print("Stock:", stock)
    print("Return:", round(stock_return, 2), "%")
    print("Status:", status)
    print("Annualized Volatility:", round(annualized_volatility, 2), "%")
    print("Risk Level:", risk_level)
    print("Investment: £", round(investment, 2))
    print("Profit/Loss: £", round(profit_loss, 2))
    print("Current Value: £", round(current_value, 2))

    stock_result = {
        "stock": stock,
        "return": stock_return,
        "volatility": annualized_volatility,
        "risk_level": risk_level,
        "investment": investment,
        "profit_loss": profit_loss,
        "current_value": current_value,
        "return_series": return_series
    }

    results.append(stock_result)

total_investment = 0
total_profit_loss = 0
total_return = 0
total_volatility = 0
high_risk_count = 0

if len(results) == 0:
    print("No stock data available")
    exit()

best_stock = results[0]
worst_stock = results[0]

for result in results:
    total_investment = total_investment + result["investment"]
    total_profit_loss = total_profit_loss + result["profit_loss"]
    total_return = total_return + result["return"]
    total_volatility = total_volatility + result["volatility"]

    if result["return"] > best_stock["return"]:
        best_stock = result

    if result["return"] < worst_stock["return"]:
        worst_stock = result

    if result["risk_level"] == "High Risk":
        high_risk_count = high_risk_count + 1

average_return = total_return / len(results)
average_volatility = total_volatility / len(results)
portfolio_return = total_profit_loss / total_investment * 100

for result in results:
    weight = result["investment"] / total_investment
    result["weight"] = weight

print("Total investment: ￡", total_investment)
print("Total Profit/Loss: ￡", round(total_profit_loss, 2))
print("Average Return: ", round(average_return, 2),"%")
print("Average Volatility: ", round(average_volatility, 2), "%")
print("Best Stock: ", best_stock["stock"])
print("Best Return: ", round(best_stock["return"], 2),"%")
print("Worst Stock: ", worst_stock["stock"])
print("Worst Return: ", round(worst_stock["return"], 2),"%")
print("Portfolio Return: ", round(portfolio_return, 2),"%")
print("High Risk Stocks: ", high_risk_count)

print("Portfolio Weights:")

for result in results:
    print(
        result["stock"], 
        "Weight:", 
        round(result["weight"] * 100, 2),
        "%"
    )

weights = []
return_data = {}

for result in results:
    weights.append(result["weight"])
    return_data[result["stock"]] = result["return_series"]

returns_df = pd.DataFrame(return_data).dropna()

correlation_matrix = returns_df.corr()

print("Correlation Matrix:")
print(correlation_matrix)

plt.figure()

plt.imshow(correlation_matrix)

plt.xticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns
)

plt.yticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns
)

plt.colorbar()
plt.title("Stock Correlation Matrix")
plt.tight_layout()
plt.show()

covariance_matrix = returns_df.cov()

weights_array = np.array(weights)

portfolio_variance = (
    weights_array.T
    @ covariance_matrix.values
    @ weights_array
)

daily_portfolio_volatility = portfolio_variance ** 0.5
portfolio_volatility = daily_portfolio_volatility * (252 ** 0.5)

print("Covariance Matrix:")
print(covariance_matrix)

if portfolio_volatility < 20:
    portfolio_risk = "Low Risk"
elif portfolio_volatility <= 40:
    portfolio_risk = "Medium Risk"
else:
    portfolio_risk = "High Risk"

print("Portfolio Volatility:", round(portfolio_volatility,2), "%")
print("Portfolio Risk:", portfolio_risk)

stock_names = []
portfolio_weights = []

for result in results:
    stock_names.append(result["stock"])
    portfolio_weights.append(result["weight"])

plt.figure()

plt.pie(
    portfolio_weights,
    labels=stock_names,
    autopct="%1.1f%%"
)

plt.title("Portfolio Allocation")
plt.tight_layout()
plt.show()