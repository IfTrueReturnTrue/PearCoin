import sockets
import datetime
from datetime import timezone
import hashlib


def hash(*args):
    hash = ""
    for arg in args:
        hash += str(arg)

    return str(hashlib.sha256(hash.encode('utf-8')).hexdigest())


class Transaction():
    def __init__ (self, sender, reciever, amount):
        self.status = "Incomplete info"
        self.timestamp = datetime.datetime.now(timezone.utc)
        self.sender = sender
        self.reciever = reciever
        self.amount = amount
        #self.sender_balance = 4
        #self.reciever_balance = 
        self.status = "Pending"

        if self.sender_balance - self.amount < 1:
            self.status = "Failed"
            del self
            # reject transaction
            # need to also send an error back to the sender

        else:
            self.status = "Approved"

#    def __str__(self):
#        return str("Sender: %s\nReciever: %s\nAmount: %s\nStatus: %s\n" 
#            %(self.sender, self.reciever ,self.amount, self.status)






class Block():
    def __init__ (self, index=0, data='', previous_hash="0" * 64, nonce=0):
        self.index = index
        self.timestamp = datetime.datetime.now(timezone.utc)
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = ''

		# try:
		# 	self.index = blockchain[-1].get('index')
		# except:
		# 	self.index = 0

		# self.timestamp = datetime.datetime.now(timezone.utc)
		# self.data = data 
                # try: 
                # 	self.previous_hash = blockchain[-1].get('hash') 
                # except: 
                # 	self.previous_hash = "0" * 64


    def hash_block(self):
        return hash(
            self.index, 
            self.timestamp, 
            self.data, 
            self.previous_hash, 
            self.nonce)


    def mine_block(self, difficulty):
        self.nonce = 0
        self.difficulty = difficulty
        self.hash_block()

        while self.hash[:difficulty] != difficulty * "0":
                self.hash = self.hash_block()
                print("hash: " + self.hash)

                self.nonce +=1
                print("nonce: " + str( self.nonce))


    def __str__(self):
        return str("Block: %s\nTimestamp: %s\nPrevious Hash: %s\nData: %s\nNonce: %s\nHash: %s\n" 
            %(self.index, self.timestamp ,self.previous_hash, self.data, self.nonce, self.hash))



class Blockchain():
    def __init__ (self):
        self.chain = []



def main():
    test_block = Block()
    test_block.mine_block(4)
    print(test_block)



if __name__ == '__main__':
    main()
