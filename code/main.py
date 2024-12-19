import os
import sys

from numberCruncher import get_stock_info, plot_stock_price, plot_yearly_returns

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


# Call the function to get general information for the provided stock symbols
get_stock_info(symbols)

# Call the function to plot the stock prices for the provided stock symbols
data = plot_stock_price(symbols)

# Call the function to plot the year-to-date returns for the provided stock symbols
plot_yearly_returns(data, symbols)
