import yfinance as yf
import sys
import os
import matplotlib.pyplot as plt
import numberCruncher

"""
    This app asks for trading symbol of a public traded company.
    Various financial data points will be downloaded from yahoo finance.
    Important indicators of the stock will be calculated.
    Some numbers will be displayed using charts by pandas.
    Depending on user input some light adjusted can be made to the output data.
"""

# Omit error print, else yf.download will always log even on success
sys.stderr = open(os.devnull, 'w')

print("")
print("#############################################")
print("##### Welcome to Stock Market Assistent #####")
print("#############################################")
print("")

try:
    symbol = str(input("Please enter tracking symbol of a publicly traded stock to start analysis: "))
    # AAPL would be a valid input as it represented Apple

except ValueError:
    print("You need to provide a string. ")

if numberCruncher.check_ticker_exists(symbol):
    # try to download stock market date for the given symbol
    data = yf.download(symbol, start="2020-01-01", end="2021-01-01")

    # Schließen-Kurse plotten
    data['Close'].plot()

    # Titel setzen
    plt.title("Apple Stock Prices")

    # show plot
    plt.show()
