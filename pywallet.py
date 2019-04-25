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
        for node in self.nodes:
            print(node)
            #r = requests.post(node, data = {'key':'value'})

    def addnode(self, node):
        self.nodes.append(node)

wallet = Pywallet()
wallet.addnode(r'https://pyblockchain.herokuapp.com/chaintest')
wallet.posttransaction(0,0)
#data = wallet.getrestjson(r'https://pyblockchain.herokuapp.com/chaintest')
#print(data)
