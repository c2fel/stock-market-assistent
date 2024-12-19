from datetime import datetime

import matplotlib.pyplot as plt
import yfinance as yf


def check_ticker_exists(tickers):
    # Ensure tickers is a list
    if isinstance(tickers, str):
        tickers = [tickers]

    # Iterate through each ticker symbol
    for ticker in tickers:
        try:
            # Fetch ticker information from Yahoo Finance
            ticker_info = yf.Ticker(ticker)
            info = ticker_info.info

            # Check if the ticker information is valid
            if not info or "address1" not in info:
                print(f"Ticker {ticker} does not exist.")
                return False
        except ValueError as e:
            # Handle any errors that occur during the fetch
            print(f"Error occurred while fetching the ticker {ticker}: {e}")
            return False

    # Return True if all tickers are valid
    return True


def plot_stock_price(symbols):
    # Check if the provided symbols exist
    if check_ticker_exists(symbols):
        # Calculate the start and end dates for the current year
        start_date = f"{datetime.now().year}-01-01"
        end_date = datetime.now().strftime("%Y-%m-%d")

        # Try to download stock market data for the given symbols for the current year-to-date
        data = yf.download(symbols, start=start_date, end=end_date)

        # Plot closing prices
        data["Close"].plot()

        # Set title
        plt.title(f"{symbols} Stock Prices")

        # Show plot
        plt.show()

        return data


# Function to get current price and general information of the symbol(s)
def get_stock_info(symbols):
    stock_info = {}
    for symbol in symbols:
        try:
            # Get ticker object from Yahoo Finance
            ticker = yf.Ticker(symbol)

            # Get the most recent closing price
            price = ticker.history(period="1d")["Close"].iloc[-1]

            # Retrieve general company information
            info = ticker.info
            listing_date = info.get("firstTradeDateEpochUtc", None)
            if listing_date:
                listing_date = datetime.fromtimestamp(listing_date).strftime("%Y-%m-%d")

            # Store stock information in a dictionary
            stock_info[symbol] = {
                "Current Price": price,
                "Company Name": info.get("longName", "N/A"),
                "Market Cap": info.get("marketCap", "N/A"),
                "Sector": info.get("sector", "N/A"),
                "Industry": info.get("industry", "N/A"),
                "Listing Date": listing_date,
            }

            # Print the stock information for each symbol
            print(f"General Information for {symbol}:")
            for key, value in stock_info[symbol].items():
                print(f"{key}: {value}")
            print("\n")

        except Exception as e:
            print(f"Error retrieving information for {symbol}: {e}")
    return stock_info


# Function to plot the returns for the current year
def plot_yearly_returns(data, symbols):
    # Calculate the cumulative returns for the current year
    returns = (
        data["Close"].pct_change().cumsum() * 100
    )  # Cumulative returns in percentage

    # Plot the cumulative returns
    returns.plot()

    # Add a horizontal line at y=0 to show the break-even point
    plt.axhline(y=0, color="black", linestyle="--", linewidth=1)

    # Set the plot title and axis labels
    plt.title(f"{symbols} Year-to-Date Returns")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return (%)")

    # Show the plot
    plt.show()
