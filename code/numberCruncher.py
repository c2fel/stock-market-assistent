import yfinance as yf


def check_ticker_exists(ticker):
    try:
        ticker_info = yf.Ticker(ticker)
        # Abrufen von allgemeinen Informationen über das Ticker-Objekt
        info = ticker_info.info
        print("")
        print(info)
        print("")
        # Wenn "info" nicht leer ist und "regularMarketPrice" vorhanden ist, dann existiert der Ticker
        if info and "address1" in info:
            # print(f"Ticker {ticker} existiert.")
            return True
        else:
            print(f"Ticker {ticker} existiert nicht.")
            return False
    except ValueError as e:
        print(f"Fehler beim Abrufen des Tickers {ticker}: {e}")
        return False
