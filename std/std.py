from pandas import DataFrame
from static.constant import Labels


def append_standard_deviations(dataframe: DataFrame, window: int, labels: Labels) -> DataFrame:
    dataframe[labels.std] = dataframe[labels.vwap].rolling(window=window).std()
    dataframe[labels.std_p1] = dataframe[labels.vwap] + dataframe[labels.std]
    dataframe[labels.std_p2] = dataframe[labels.vwap] + (dataframe[labels.std] * 2)
    dataframe[labels.std_m1] = dataframe[labels.vwap] - dataframe[labels.std]
    dataframe[labels.std_m2] = dataframe[labels.vwap] - (dataframe[labels.std] * 2)
    return dataframe

