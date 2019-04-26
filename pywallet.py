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
            j = requests.post(address, json = {'sender':"James",'recipient':recipient,'amount':amt}).json()
            print(j)
        return

    def addnodeclient(self, node):
        self.nodes.append(node)

    def addnodeserver(self, node):
        for node in self.nodes:
            address = node+"/nodes/register"
            j = requests.post(address, json = {'nodes':node}).json()
        print(j)
        return

wallet = Pywallet()

wallet.addnodeclient(r'https://pyblockchain.herokuapp.com')
wallet.addnodeclient(r'https://pyblockchain2.herokuapp.com')

wallet.addnodeserver(r'https://pyblockchain.herokuapp.com')
wallet.addnodeserver(r'https://pyblockchain2.herokuapp.com')

#wallet.posttransaction("Jorge","9")
