from pandas import DataFrame
from static.constant import Labels


def append_vwap(dataframe: DataFrame, window: int, labels: Labels) -> DataFrame:
    dataframe[labels.vwap] = (
        ((dataframe[labels.close] * dataframe[labels.volume]).rolling(window=window)).mean() /
        dataframe[labels.volume].rolling(window=window).mean()
    )
    return dataframe