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
        r = requests.get(address).json()
        print(r)
        return

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
            print("adding: "+node)
            address = node+"/nodes/register"
            j = requests.post(address, json = {'nodes':node}).json()
        print(j)
        return

    def verifybalance(self, uid):
        for node in self.nodes:
            address = node+"/checkbalance"
            j = requests.post(address, json = {'uid':uid}).json()
        print(j)
        return


wallet = Pywallet()

#wallet.addnodeclient(r'https://pyblockchain.herokuapp.com')
#wallet.addnodeclient(r'https://pyblockchain2.herokuapp.com')

#print("current nodes")
#print(*wallet.nodes)

#wallet.addnodeserver(r'https://pyblockchain.herokuapp.com')
#wallet.addnodeserver(r'https://pyblockchain2.herokuapp.com')

print(r'getting json https://pyblockchain.herokuapp.com/getnodes') 
wallet.getrestjson(r'https://pyblockchain.herokuapp.com/getnodes'+'\n')

print(r'getting json https://pyblockchain2.herokuapp.com/getnodes')
wallet.getrestjson(r'https://pyblockchain2.herokuapp.com/getnodes')

#wallet.posttransaction("Jorge","9")
