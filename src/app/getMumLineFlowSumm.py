from src.typeDefs.appConfig import IAppConfig
from src.services.scadaApiFetcher import ScadaApiFetcher
from src.utils.numUtils import sumWithNone
import datetime as dt
from operator import attrgetter
from src.typeDefs.lineFlowSumm import ILineFlowSumm


def getMumbaiLineFlowSumm(appConfig: IAppConfig) -> ILineFlowSumm:
    scadaApiHost = appConfig['scadaApiHost']
    scadaApiPort = appConfig['scadaApiPort']
    isDummyFetch = True if appConfig['dummyFetch'] == 1 else False
    # get an instance of scada fetcher
    fetcher = ScadaApiFetcher(scadaApiHost, scadaApiPort, isDummyFetch)

    # get the required point Ids and installed capacities
    flowKeys = ['khargPuneMw_4', 'kalwPadg1Mw_4', 'kalwPadg2Mw_4', 'kalwPuneMw_4', 'kalwKhargMw_4', 'kalwKhargMw_2', 'kharNerMw_2', 'boisNalMw_2', 'boisBois1Mw_2',
                'boisBois2Mw_2', 'boisBois3Mw_2', 'boisBorivMw_2', 'borivTarapMw_2', 'kalwSal1Mw_2', 'kalwSal2Mw_2', 'chanPad1Mw_h', 'chanPad2Mw_h', 'mumbaiDemand']

    currTime = dt.datetime.now()
    dayStartTime = dt.datetime(currTime.year, currTime.month, currTime.day)
    # create instantaneous line flows
    instFlowDict: dict = {}
    maxFlowDict: dict = {}
    maxFlowTimeDict: dict = {}
    for fkey in flowKeys:
        lineFlowHist = fetcher.fetchPntHistData(
            appConfig[fkey], dayStartTime, currTime, 'snap', 60)
        instFlowDict[fkey] = None
        maxFlowDict[fkey] = None
        maxFlowTimeDict[fkey] = None
        if len(lineFlowHist) == 0:
            continue
        instFlowDict[fkey] = int(lineFlowHist[-1]["dval"])
        # derive the sample with max dval property
        maxFlowObj = lineFlowHist[0]
        for fObj in lineFlowHist:
            if abs(fObj['dval']) > abs(maxFlowObj['dval']):
                maxFlowObj = fObj
        maxFlowDict[fkey] = int(maxFlowObj['dval'])
        maxFlowTimeDict[fkey] = maxFlowObj['timestamp'][11:16]
    return {'inst': instFlowDict, 'maxFlow': maxFlowDict, 'maxTime': maxFlowTimeDict}
