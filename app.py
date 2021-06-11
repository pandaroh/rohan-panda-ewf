#!/usr/bin/env python3
from flask import Flask, render_template
from requests import Request, Session
import json

class CryptoPrice:

    def get_top_20(self):

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
          'start':'1',
          'limit':'20',
          'convert':'USD'
        }
        headers = {
          'Accepts': 'application/json',
          'X-CMC_PRO_API_KEY': '6c51348a-7cd7-49b5-9504-fa6b5e6ada84',
        }

        session = Session()
        session.headers.update(headers)

        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data['data']

app = Flask(__name__)
cryptoPrice = CryptoPrice()

@app.route("/")
def getprice():
    results = cryptoPrice.get_top_20()


    for result in results:
        result['quote']['USD']['price'] = '$ ' + "{:.2f}".format(result['quote']['USD']['price'])

    return render_template('index.html', **locals())

if __name__ == "__main__":
    app.run(host='0.0.0.0')
