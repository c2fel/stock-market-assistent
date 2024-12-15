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
