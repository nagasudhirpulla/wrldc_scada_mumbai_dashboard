from typing import TypedDict


class IAppConfig(TypedDict):
    flaskSecret: str
    flaskPort: str
    mode: str
    dummyFetch: float
    scadaApiHost: str
    scadaApiPort: int
    tataBhiraIC: float
    tataBhiraGen: str
    tataBhiraPssIC: float
    tataBhiraPssGen: str
    tataBhivIC: float
    tataBhivGen: str
    tataKhopIC: float
    tataKhopGen: str
    tataU5IC: float
    tataU5Gen: str
    tataU7AIC: float
    tataU7AGen: str
    tataU7BIC: float
    tataU7BGen: str
    tataU8IC: float
    tataU8Gen: str
    dahanuU1IC: float
    dahanuU1Gen: str
    dahanuU2IC: float
    dahanuU2Gen: str
    khargPuneMw_4: str
    kalwPadg1Mw_4: str
    kalwPadg2Mw_4: str
    kalwPuneMw_4: str
    kalwKhargMw_4: str
    kalwKhargMw_2: str
    kharNerMw_2: str
    boisNalMw_2: str
    boisBois1Mw_2: str
    boisBois2Mw_2: str
    boisBois3Mw_2: str
    boisBorivMw_2: str
    borivTarapMw_2: str
    kalwSal1Mw_2: str
    kalwSal2Mw_2: str
    chanPad1Mw_h: str
    chanPad2Mw_h: str