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
