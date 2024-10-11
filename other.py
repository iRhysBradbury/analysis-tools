import yfinance as yf
import matplotlib.pyplot as plt
from dataclasses import dataclass
from std import std
from vwap import vwap
tickers = ["BTC-USD"]

interval = 7
start = "2020-06-01"
end = "2020-10-31"

data = yf.download(
    tickers=tickers,
    start=start,
    end=end
)

@dataclass
class Colors:
    blue: str
    dark_grey: str
    light_grey: str

@dataclass
class Labels:
    vwap: str
    close: str
    volume: str
    std: str
    std_m1: str
    std_m2: str
    std_p1: str
    std_p2: str
    colors: Colors

labelsData = Labels(
    vwap="VWAP",
    close="Close",
    volume="Volume",
    std="Standard Deviation",
    std_m1="Standard Deviation M1",
    std_m2="Standard Deviation M2",
    std_p1="Standard Deviation P1",
    std_p2="Standard Deviation P2",
    colors=Colors(
        blue="#0014c7",
        dark_grey="#5b5e5d",
        light_grey="#b2b3af"
    )
)

dataWVWAP = vwap.append_vwap(
    dataframe=data,
    window=interval,
    labels=labelsData
)
dataMutated = std.append_standard_deviations(
    dataframe=dataWVWAP,
    window=interval,
    labels=labelsData
)

dataNoNaN = dataMutated.dropna()