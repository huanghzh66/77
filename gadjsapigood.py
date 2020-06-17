# coding=utf-8

from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import json

app = Flask(__name__)


@app.route('/')
def files():
    return render_template("gadjsapigood.html")


@app.route('/gpsarr', methods=['POST', 'GET'])
def gpsarr():
    gpsArray = []
    if request.method == 'POST':
        gpsArray = request.data.decode('utf-8')
        gpsArray = gpsArray.replace("|", ",")
        gps_list = gpsArray.split(',')
        interval = 2
        gps_set = []
        if (len(gps_list) % 2 == 0):
            for idx in range(0, len(gps_list), 2):
                gps_set.append([gps_list[idx], gps_list[idx + 1]])
        df = pd.DataFrame(gps_set, columns=['lng', 'lat'])
        df.to_excel("e:/gpsapp.xlsx", index=False)
    if request.method == 'GET':
        data = pd.read_excel('e:/gpsapp.xlsx')
        gps_data = np.array(data)
        gpsArray = gps_data.tolist()
        gpsArray = json.dumps(gpsArray, ensure_ascii=False)
    return gpsArray


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=80 ,debug=True)
    app.run(host='0.0.0.0', port=80)
