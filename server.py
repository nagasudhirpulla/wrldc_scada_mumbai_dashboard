from src.config.appConfig import getConfig
from flask import Flask, request, jsonify, render_template
from src.app.getMumIntRtGen import getMumbaiIntGen
import datetime as dt

app = Flask(__name__)

# get application config
appConfig = getConfig()

# Set the secret key to some random bytes
app.secret_key = appConfig['flaskSecret']


@app.route('/')
def index():
    currTime = dt.datetime.now()
    currTimeStr = dt.datetime.strftime(currTime, "%d-%b-%Y %H:%M")
    internalGen = getMumbaiIntGen(appConfig)
    return render_template('index.html.j2', gen=internalGen, currTime=currTimeStr)


if __name__ == '__main__':
    serverMode: str = appConfig['mode']
    app.run(host="0.0.0.0", port=int(appConfig['flaskPort']), debug=True)
