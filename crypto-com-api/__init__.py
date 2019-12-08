#!/usr/bin/python
# coding: utf8

import requests

class CryptoComApi():
    def __init__(self, token = "", secret_key = ""):
        self.url = "https://api.crypto.com"
        self.token = token
        self.secret_key = secret_key
        
    def get_symbols(self):
        return requests.get(self.url + "/v1/symbols").json()['data']
    
    def get_k_lines(self, symbol, period, format_data = False):
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
