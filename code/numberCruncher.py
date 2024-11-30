import yfinance as yf


def check_ticker_exists(ticker):
    try:
        ticker_info = yf.Ticker(ticker)
        # Abrufen von allgemeinen Informationen über das Ticker-Objekt
        info = ticker_info.info

        """
            Idea to improve: The data which is pulled from yahoo finance is redundant
                (1) check_ticker_exists() calls yf.Ticker(ticker)
                (2) yf.download(symbol, start="2020-01-01", end="2021-01-01") is called in main.py
                (3) yf.Ticker(symbol) is called in main.py
                
                This could be done with one call to yahoo finance, while the ticker is still being validated
        """

        # Wenn "info" nicht leer ist und "regularMarketPrice" vorhanden ist, dann existiert der Ticker
        if info and "address1" in info:
            # print(f"Ticker {ticker} existiert.")
            return True
        else:
            print(f"Ticker {ticker} does not exist.")
            return False
    except ValueError as e:
        print(f"Error occurred while fetching the ticker {ticker}: {e}")
        return False


"""
    add more functionality here
    
    (1) Create a one page report in a PDF format including financial numbers and charts about the company
        more information: https://realpython.com/creating-modifying-pdf/#creating-pdf-files-with-python-and-reportlab
        
    (2) Get an investment recommendation regarding the stock from openAi API
"""
