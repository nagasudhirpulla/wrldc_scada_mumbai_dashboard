import requests
import json
import datetime as dt
from typing import Dict, Union, List, Optional
from src.typeDefs.scadaApiDataSample import IScadaApiDataSample
import pandas as pd
import random


class ScadaApiFetcher():
    apiHost: str = ''
    apiPort: int = 80
    isDummyFetch: bool = False

    def __init__(self, apiHost: str, apiPort: int, isDummyFetch=False):
        self.apiHost = apiHost
        self.apiPort = apiPort
        self.isDummyFetch = isDummyFetch

    def fetchPntHistData(self, pnt: str, startTime: dt.datetime, endTime: dt.datetime, fetchStrategy: str = 'snap', sampleFreq: int = 300) -> List[IScadaApiDataSample]:
        if self.isDummyFetch:
            if (startTime > endTime) or (sampleFreq == 0):
                return []
            currTime = startTime
            dataRes: List[IScadaApiDataSample] = []
            while currTime <= endTime:
                dataRes.append(
                    {"timestamp": currTime, "dval": random.randint(1, 100), "status": "GOOD"})
                currTime = currTime + dt.timedelta(seconds=sampleFreq)
            return dataRes
        startTimeStr = startTime.strftime('%d/%m/%Y/%H:%M:%S')
        endTimeStr = endTime.strftime('%d/%m/%Y/%H:%M:%S')
        # print(req_date_str)
        params: Dict[str, Union[int, str]] = dict(
            pnt=pnt,
            strtime=startTimeStr,
            endtime=endTimeStr,
            secs=sampleFreq,
            type=fetchStrategy
        )
        try:
            # http://host:80/api/values/history?pnt=pntId&strtime=12/12/2019/00:00:00&endtime=13/12/2019/00:00:00&secs=900&type=average
            r = requests.get(
                url="http://{0}:{1}/api/values/history".format(self.apiHost, self.apiPort), params=params)
            resTxt = r.text
            if pd.isna(resTxt) or (resTxt == '') or (resTxt == '[]') or (resTxt == 'null'):
                return []
            data = json.loads(resTxt)
            return data
        except:
            return []

    def fetchPntRtData(self, pnt) -> Optional[float]:
        if self.isDummyFetch:
            return random.randrange(1, 100)
        params = dict(
            pnt=pnt,
        )
        try:
            # http://host:80/api/values/real?pnt=pntId&strtime=12/12/2019/00:00:00&endtime=13/12/2019/00:00:00&secs=900&type=average
            r = requests.get(
                url="http://{0}:{1}/api/values/real".format(self.apiHost, self.apiPort), params=params)
            resTxt = r.text
            if pd.isna(resTxt) or (resTxt == ''):
                return None
            return float(r.text)
        except:
            return None
