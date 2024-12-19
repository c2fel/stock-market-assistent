import os
import sys
from datetime import datetime

import matplotlib.pyplot as plt
import numberCruncher
import yfinance as yf

"""
    This app asks for trading symbol of a public traded company.
    Various financial data points will be downloaded from yahoo finance.
    Important indicators of the stock will be calculated.
    Some numbers will be displayed using charts by pandas.
    Depending on user input some light adjusted can be made to the output data.
"""

# Omit error print, else yf.download will always log even on success
sys.stderr = open(os.devnull, "w")

print("")
print("#############################################")
print("##### Welcome to Stock Market Assistent #####")
print("#############################################")
print("")

try:
    print(
        "You can enter multiple trading symbols (e.g. AAPL, MSFT, TSLA) in a comma separated list."
    )
    print(
        "The app will then fetch the data for each symbol in the current year and displays"
    )
    print("a comparison.")
    symbol = str(
        input(
            "Please enter tracking symbol(s) of a publicly traded stock to start the analysis: "
        )
    )
    # Parse the input string and create a list of symbols
    symbols = [s.strip() for s in symbol.split(",")]

except ValueError:
    print("You need to provide a string.")

# Check if the provided symbols exist
if numberCruncher.check_ticker_exists(symbols):
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


    # Function to get current price and general information of the symbol(s)
    def get_stock_info(symbols):
        stock_info = {}
        for symbol in symbols:
            try:
                # Get ticker object from Yahoo Finance
                ticker = yf.Ticker(symbol)
                
                # Get the most recent closing price
                price = ticker.history(period="1d")['Close'].iloc[-1]
                
                # Retrieve general company information
                info = ticker.info
                listing_date = info.get("firstTradeDateEpochUtc", None)
                if listing_date:
                    listing_date = datetime.fromtimestamp(listing_date).strftime("%Y-%m-%d")

                # Store stock information in a dictionary
                stock_info[symbol] = {
                    'Current Price': price,
                    'Company Name': info.get("longName", "N/A"),
                    'Market Cap': info.get("marketCap", "N/A"),
                    'Sector': info.get("sector", "N/A"),
                    'Industry': info.get("industry", "N/A"),
                    'Listing Date': listing_date
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
        returns = data["Close"].pct_change().cumsum() * 100  # Cumulative returns in percentage
        
        # Plot the cumulative returns
        returns.plot()
        
        # Add a horizontal line at y=0 to show the break-even point
        plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
        
        # Set the plot title and axis labels
        plt.title(f"{symbols} Year-to-Date Returns")
        plt.xlabel("Date")
        plt.ylabel("Cumulative Return (%)")
        
        # Show the plot
        plt.show()

    # Call the function to get general information for the provided stock symbols
    get_stock_info(symbols)
    
    # Call the function to plot the year-to-date returns for the provided stock symbols
    plot_yearly_returns(data, symbols)
