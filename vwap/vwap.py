from pandas import DataFrame
from main import Labels


def append_vwap(dataframe: DataFrame, window: int, labels: Labels):
    dataframe[labels.vwap] = (
        ((dataframe[labels.close] * dataframe[labels.volume]).rolling(window=window)).mean() /
        dataframe[labels.volume].rolling(window=window).mean()
    )
    return dataframe