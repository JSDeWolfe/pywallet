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

    def verifybalance(self, url,uid):
        address = url+"/getbalance"
        j = requests.get(address, json = {'uid':uid}).json()
        print(j)
        return


wallet = Pywallet()

wallet.verifybalance(r'https://pyblockchain.herokuapp.com', "dfs")

#print("initial check")
#print("pbc")
#wallet.getrestjson(r'https://pyblockchain.herokuapp.com/getnodes'+'\n')
#print("pbc2")
#wallet.getrestjson(r'https://pyblockchain.herokuapp.com/getnodes'+'\n')

#wallet.addnodeclient(r'https://pyblockchain.herokuapp.com')
#wallet.addnodeclient(r'https://pyblockchain2.herokuapp.com')

#print("current nodes")
#print(*wallet.nodes)
#print("adding nodes to first server")
#wallet.addnodeserver(r'https://pyblockchain.herokuapp.com')
#print("checking nodes first server")
#wallet.getrestjson(r'https://pyblockchain.herokuapp.com/getnodes'+'\n')
#print("adding nodes to second server")
#wallet.addnodeserver(r'https://pyblockchain2.herokuapp.com')
#print("checking nodes second server")
#wallet.getrestjson(r'https://pyblockchain2.herokuapp.com/getnodes')

#wallet.posttransaction("Jorge","9")
