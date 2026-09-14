# Stock Portfolio Risk Analyzer

A Python-based stock portfolio analysis tool that uses historical price data to evaluate stock performance and portfolio risk.

## Features

- Analyze multiple stocks from historical CSV data
- Calculate stock returns and profit/loss
- Calculate annualized historical volatility
- Classify stocks into different risk levels
- Calculate portfolio weights
- Identify the best and worst performing stocks
- Calculate correlation and covariance between stock returns
- Calculate portfolio volatility using portfolio weights and covariance
- Visualize historical stock prices
- Visualize daily returns
- Visualize portfolio allocation
- Visualize stock correlations

## Technologies Used

- Python
- pandas
- NumPy
- Matplotlib

## How It Works

The program reads historical stock price data from CSV files and analyzes both individual stocks and the overall portfolio.

### 1. Stock Return

The program compares the user's buy price with the latest closing price to calculate the percentage return.

It also calculates the profit or loss based on the amount invested in each stock.

### 2. Historical Volatility

Daily returns are calculated from historical closing prices.

The program uses the sample standard deviation of daily returns to estimate daily volatility. It then annualizes the volatility using 252 trading days.

Annualized Volatility = Daily Volatility × √252

### 3. Risk Classification

Stocks are classified using the following project-defined thresholds:

- Low Risk: volatility below 20%
- Medium Risk: volatility between 20% and 40%
- High Risk: volatility above 40%

These thresholds are used for demonstration purposes and are not universal investment risk standards.

### 4. Portfolio Analysis

The program calculates the weight of each stock based on the amount invested.

It then aligns the historical return data by date and calculates:

- Correlation matrix
- Covariance matrix
- Portfolio variance
- Annualized portfolio volatility

Portfolio variance is calculated using the portfolio weight vector and covariance matrix:

Portfolio Variance = wᵀΣw

where `w` represents portfolio weights and `Σ` represents the covariance matrix.

### 5. Data Visualization

The program creates charts for:

- Historical stock prices
- Daily stock returns
- Portfolio allocation
- Stock return correlations

## Data Format

The program uses historical stock price data stored in CSV files.

Each CSV file should be named using the stock ticker, for example:

- `AAPL.csv`
- `TSLA.csv`
- `MSFT.csv`

The CSV file must contain at least the following columns:

- `Date`
- `Close/Last`

Example:

| Date | Close/Last |
| --- | --- |
| 09/11/2026 | $332.27 |
| 09/10/2026 | $329.12 |
| 09/09/2026 | $326.45 |

The program automatically converts the date column, removes the `$` symbol from closing prices, and sorts the data by date.

For portfolio analysis, at least two stocks are required.

## How to Run

1. Clone or download this repository.

2. Install the required Python libraries:

   `python -m pip install -r requirements.txt`

3. Place the historical CSV files in the same folder as `stock_analyzer.py`.

4. Run the program:

   `python stock_analyzer.py`

5. Enter the requested information, including:

   - Number of stocks
   - Stock name
   - Stock ticker
   - Buy price
   - Investment amount

The program will calculate the results and display the portfolio analysis and charts.

## Example Output

Example portfolio analysis:

```text
Total Investment: £850.00
Total Profit/Loss: £698.48
Average Return: 68.44%
Average Volatility: 34.71%

Best Stock: Microsoft
Worst Stock: Tesla

Portfolio Return: 82.17%

Portfolio Weights:
Apple: 35.29%
Tesla: 23.53%
Microsoft: 41.18%

Portfolio Volatility: 22.52%
Portfolio Risk: Medium Risk

```

The exact results depend on the historical data, buy prices, and investment amounts entered by the user.

## Project Structure

```text
stock-portfolio-risk-analyzer/
│
├── stock_analyzer.py
├── requirements.txt
└── README.md
```

Historical CSV files should be placed in the project folder before running the program.

## Disclaimer

This project is for educational and portfolio demonstration purposes only.

The calculations are based on historical market data and do not predict future stock performance. The risk classifications used by the program are project-defined and should not be considered investment advice.