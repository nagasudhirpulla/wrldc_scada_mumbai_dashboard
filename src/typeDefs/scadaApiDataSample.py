from typing import TypedDict
import datetime as dt


class IScadaApiDataSample(TypedDict):
    timestamp: dt.datetime
    dval: float
    status: str