import unittest
from src.services.scadaApiFetcher import ScadaApiFetcher
from src.config.appConfig import getConfig
import datetime as dt


class TestBayOwnersFetcher(unittest.TestCase):
    appConfig: dict = {}

    def setUp(self):
        self.appConfig = getConfig()

    def test_dummyFetch(self) -> None:
        """tests the dummy fetch feature of scada api fetcher
        """
        fetcher = ScadaApiFetcher("", 80, True)
        endTime = dt.datetime.now()
        startTime = endTime - dt.timedelta(hours=1)
        
        data = fetcher.fetchPntHistData("", startTime, endTime, 'snap', 60)
        self.assertFalse(len(data) == 0)
        
        data = fetcher.fetchPntRtData("")
        self.assertIsNotNone(data)