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

    def posttransaction(self, recipient, amt):
        for node in self.nodes:
            address = node+"/posttransaction"
            j = requests.post(address, json = {'sender':"self",'recipient':recipient,'amount':amt})
            print(j)
        return

    def addnode(self, node):
        self.nodes.append(node)

wallet = Pywallet()
wallet.addnode(r'https://pyblockchain.herokuapp.com')
#wallet.addnode(r'https://pyblockchain.herokuapp.com/chaintest')
wallet.posttransaction("jorge","9")
#data = wallet.getrestjson(r'https://pyblockchain.herokuapp.com/chaintest')
#print(data)
