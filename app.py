from flask import Flask, render_template, jsonify
import pandas as pd
from six.moves import urllib
import json
 
app = Flask(__name__)
 
@app.route("/data.json")
def data():
    timeInterval = 1000
    data = pd.DataFrame()
    featureList = ['market-price', 
                   'trade-volume']
    for feature in featureList:
        url = "https://api.blockchain.info/charts/"+feature+"?timespan="+str(timeInterval)+"days&format=json"
        data['time'] = pd.DataFrame(json.loads(urllib.request.urlopen(url).read().decode('utf-8'))['values'])['x']*1000
        data[feature] = pd.DataFrame(json.loads(urllib.request.urlopen(url).read().decode('utf-8'))['values'])['y']
    result = data.to_dict(orient='records')
    seq = [[item['time'], item['market-price'], item['trade-volume']] for item in result]
    return jsonify(seq)
 
@app.route("/")
def index():
    return render_template('index.html')
 
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)