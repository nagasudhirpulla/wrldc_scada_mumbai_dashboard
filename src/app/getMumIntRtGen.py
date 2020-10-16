from src.typeDefs.appConfig import IAppConfig
from src.services.scadaApiFetcher import ScadaApiFetcher
from src.utils.numUtils import sumWithNone


def getMumbaiIntGen(appConfig: IAppConfig) -> dict:
    scadaApiHost = appConfig['scadaApiHost']
    scadaApiPort = appConfig['scadaApiPort']
    isDummyFetch = True if appConfig['dummyFetch'] == 1 else False
    # get an instance of scada fetcher
    fetcher = ScadaApiFetcher(scadaApiHost, scadaApiPort, isDummyFetch)

    # get the required point Ids and installed capacities
    instKeys = ['tataBhiraIC', 'tataBhiraPssIC', 'tataBhivIC', 'tataKhopIC', 'tataU5IC', 'tataU7AIC', 'tataU7BIC', 'tataU8IC', 'dahanuU1IC', 'dahanuU2IC']
    genKeys = ['tataBhiraGen', 'tataBhiraPssGen', 'tataBhivGen', 'tataKhopGen',
               'tataU5Gen', 'tataU7AGen', 'tataU7BGen', 'tataU8Gen', 'dahanuU1Gen', 'dahanuU2Gen']

    # create generation info installed capacity
    genData = {}
    for instKey in instKeys:
        genData[instKey] = appConfig[instKey]

    # create generation info current generation
    for genKey in genKeys:
        genData[genKey] = fetcher.fetchPntRtData(appConfig[genKey])

    # total generation
    genData['totalGen'] = sumWithNone(*[genData[genKey] for genKey in genKeys])
    # populate mumbai demand
    genData['mumbaiDemand'] = fetcher.fetchPntRtData(appConfig['mumbaiDemand'])
    return genData
