#!/usr/bin/env python3

import json
import requests
import tools.SMS.phonenumbers as numberTools
import tools.SMS.randomdata as randomData




class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'

def getServices(file = 'tools/SMS/services.json'):
    with open(file, 'r') as services:
        return json.load(services)["services"]


def getProxys(file = 'tools/SMS/proxy.json'):
    with open(file, 'r') as proxys:
        return json.load(proxys)["proxy"]


def getDomain(url):
    return url.split('/')[2]


class Service:
    def __init__(self, service):
        self.service = service
        self.proxy = getProxys()
        self.timeout = 10

    # Parse string
    def parseData(self, phone):
        payload = None
        # Check for 'data'
        try:
            dataType = "data"
            payload = self.service["data"]
        except KeyError:
            pass

        try:
            dataType = "json"
            payload = self.service["json"]
        except KeyError:
            pass

        if not payload:
            payload = json.dumps({"url": self.service["url"]})
            dataType = "url"

        for old, new in {
            "\'": "\"",
            "%phone%": phone,
            "%phone5%": numberTools.transformPhone(phone, 5),
            "%name%":  randomData.random_name(),
            "%email%": randomData.random_email(),
            "%password%": randomData.random_password()
            }.items():
            payload = payload.replace(old, new)
        return (json.loads(payload), dataType)
    

    def sendMessage(self, phone):
        url = self.service["url"]
        
        payload, dataType = self.parseData(phone)

        # Headers for request
        headers = {
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Accept-Encoding": "gzip, deflate, br",
            "User-agent": randomData.random_useragent()
            }


        try:
            customHeaders = self.service["headers"]
        except KeyError:
            pass
        else:
            for key, value in json.loads(customHeaders.replace("\'", "\"")).items():
                headers[key] = value


        okay  = "Service (" + getDomain(url) + ") >> message sent"
        error = "Service (" + getDomain(url) + ") >> can t send the msg error."

        try:

            if dataType == "json":
                r = requests.post(url, json = payload, timeout = self.timeout, headers = headers, proxies = self.proxy)

            elif dataType == "data":
                r = requests.post(url, data = payload, timeout = self.timeout, headers = headers, proxies = self.proxy)
            elif dataType == "url":
                r = requests.post(payload["url"], timeout = self.timeout, headers = headers, proxies = self.proxy)


            if r.status_code == 200:
                print(bcolors.OKGREEN + "[+]"+  okay)
            elif r.status_code == 429:
                print(bcolors.WARNING + "[!]" + error)
            else:

                print(bcolors.WARNING + "[!]" + error)
            
            return r.status_code

        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
            print("[!]" + error)
        except (requests.exceptions.ConnectionError):
            print("[!]" + error)
