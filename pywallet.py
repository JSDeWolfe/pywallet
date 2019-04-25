import hashlib
import requests
import json

class Pywallet(object):

    def __init__(self):
        self.balance = []
        self.transactionrequest = []
        self.nodes = []
        self.idhash = []
        

    def getrestjson(self, address):
        r = requests.get(address)
        data = r.json()
        return data

    def posttransaction(self, otherparty, amt):
        for node in nodes:
            r = requests.post(node, data = {'key':'value'})

wallet = Pywallet()

data = wallet.getrestjson(r'https://pyblockchain.herokuapp.com/chaintest')
print(data)
