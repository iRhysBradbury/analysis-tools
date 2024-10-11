import yfinance as yf
from pandas import DataFrame


def data(tickers: list[str], start: str, end: str) -> DataFrame:
    return yf.download(
        tickers=tickers,
        start=start,
        end=end
    )
