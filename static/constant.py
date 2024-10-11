from dataclasses import dataclass


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
