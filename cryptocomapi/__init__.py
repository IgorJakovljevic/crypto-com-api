#!/usr/bin/python
# coding: utf8

import requests
import hashlib
import datetime

class CryptoComApi():
    def __init__(self, api_key="", secret_key=""):
        self.url = "https://api.crypto.com"
        self.api_key = api_key
        self.secret_key = secret_key

    def get_symbols(self):
        """ Queries all transaction pairs and precision supported by the system

        Returns:
            [list] -- list of all transaction pairs and precision supported by the system
        """

        return requests.get(self.url + "/v1/symbols").json()['data']

    def get_ticker(self, symbol):
        """ Gets the current market quotes

        Arguments:
            symbol {string} -- Market mark e.g. btcusdt

        Returns:
            [dict] -- Returns current market quotes of the given symbol.
        """

        request_url = f"{self.url}/v1/ticker?symbol={symbol}"
        return requests.get(request_url).json()['data']

    def get_trades(self, symbol):
        """ Obtains market transaction records.

        Arguments:
            symbol {string} -- Market mark e.g. btcusdt

        Returns:
            [list] -- Returns a list of market transaction records
        """
        request_url = f"{self.url}/v1/trades?symbol={symbol}"
        return requests.get(request_url).json()['data']

    def get_market_trades(self):
        """ Gets the latest transaction price of each pair of currencies

        Arguments:
            symbol {string} -- Market mark e.g. btcusdt

        Returns:
            [list] -- List of latest transaction price of each pair of currencies
        """
        request_url = f"{self.url}/v1/ticker/price"
        return requests.get(request_url).json()['data']

    def get_orders(self, symbol, step="step1"):
        """ Gets the list of orders from buyers and sellers for the market

        Arguments:
            symbol {[string]} -- Market mark, ethbtc, See below for details

        Keyword Arguments:
            step {str} -- The depth type -- options: step0, step1, step2 (Merger depth0-2).
                step0time is the highest accuracy (default: {"step1"})

        Returns:
            [list] -- List of orders from buyers and sellers for the market
        """
        request_url = f"{self.url}/v1/depth?symbol={symbol}&type={step}"
        return requests.get(request_url).json()['data']

    def get_k_lines(self, symbol, period, format_data=False):
        """ Gets K-line data for symbol for a given period

        Arguments:
            symbol {string} -- Market mark e.g. bchbtc
            period {int} -- Given in minutes. Possible values are [1, 5, 15, 30, 60, 1440, 10080, 43200]
                    which corresponds to 1min, 5min, 15min, 30min, 1hour, 1day, 1week, 1month.

        Keyword Arguments:
            format_data {bool} -- If set to true the output elements are formated as a dictionary (default: {False})

        Returns:
            [list] -- Returns K-line data for symbol for a given period
        """
        request_url = f"{self.url}/v1/klines?symbol={symbol}&period={period}"
        data = requests.get(request_url).json()['data']
        if(not format_data):
            return data

        def parse_obj(val):
            ret = dict()
            ret["ts"] = val[0]
            ret["open"] = val[1]
            ret["high"] = val[2]
            ret["min"] = val[3]
            ret["close"] = val[4]
            ret["volume"] = val[5]
            return ret
        return [parse_obj(x) for x in data]

   
    def sign(self, params: dict):
        sign_str = ""
        # sort params alphabetically and add to signing string
        for param in sorted(params.keys()):
            sign_str += param + str(params[param])
        # at the end add the secret
        sign_str += str(self.secret_key)
        hash = hashlib.sha256(sign_str.encode()).hexdigest()
        return hash

    def mandatory_post_params(self):
        data = dict()
        data['api_key'] = self.api_key
        data['time'] = int(datetime.datetime.now().timestamp() * 1000)
        return data

    def get_account(self):
        data = self.mandatory_post_params()
        data['sign'] = self.sign(data)
        
        request_url = f"{self.url}/v1/account"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        return requests.post(request_url, data=data, headers =headers).json()

    def get_open_orders(self, symbol):
        data = self.mandatory_post_params()
        data['symbol'] = symbol
        data['sign'] = self.sign(data)

        request_url = f"{self.url}/v1/openOrders"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        return requests.post(request_url, data=data, headers =headers).json()
        
