# -*- coding: UTF-8 -*-
from flask import Flask, request, jsonify

import pymysql

annie_sql = {
    "host" : "104.199.195.56",
    "user" : "annie",
    "passwd" : "Annie@2021",
    "db" : "cloth",
    "charset" : "utf8"
}

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask API started'

@app.route('/allcloth', methods=['GET'])
def all_clothes():
    e = pymysql.connect(**annie_sql)
    c = e.cursor()
    c.execute("SELECT * FROM `AllCloth` order by -ID desc")
    r = c.fetchall()
    e.close()
    return jsonify({'allcloth': r})

@app.route('/newarrival', methods=['GET'])
def new_arrival():
    e = pymysql.connect(**annie_sql)
    c = e.cursor()
    c.execute("SELECT * FROM `NewArrival` order by -ID desc")
    r = c.fetchall()
    e.close()
    return jsonify({'newarrival': r})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
