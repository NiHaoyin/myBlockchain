from hashlib import sha256
import common
import time
import random


class block:
    # a block header contains 
    # the hash value of its previous block, nonce, transaction root and time stamp
    # the difficulty of digging out a block is set to 000 by default
    def __init__(self, previous_hash, difficulty="000"):
        self.previous_hash = previous_hash
        self.nonce = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba',8))
        self.tx_root = common.gen_tx_root()
        self.time_stamp = time.time()
        self.t = difficulty  # the difficulty to mine a block

    def mining(self):
        start_time = time.time()  # record the time when you start mining 
        while True:
            nonce = common.gen_nonce()
            self.time_stamp = time.time()  # update the time stamp before one iteration
            # successfully dig out a block
            if self.check(nonce):
                self.nonce = nonce
                break
            else:
                continue
        end_time = time.time()  # record the time when you finish mining
        mining_time = end_time - start_time
        print("mining time is:", mining_time)
        self.display()


    def display(self):
        print("previous hash is:", self.previous_hash)
        print("nonce is:", self.nonce)
        print("tx_root is:", self.tx_root)
        print("time stamp is:", self.time_stamp) 
        print("difficulty is:", self.t)

    #  if the current hash value is less than t, return True else return False
    def check(self, nonce):
        s = sha256()
        s.update(self.previous_hash.encode("utf-8"))
        s.update(nonce.encode("utf-8"))  
        s.update(self.tx_root.encode("utf-8"))
        s.update(str(self.time_stamp).encode("utf-8"))
        hash_value = s.hexdigest()
        return hash_value.startswith(self.t)


if __name__ =="__main__":
    s = sha256()
    s.update("nihao".encode("utf-8"))
    initial_hash = s.hexdigest()
    new_block = block(initial_hash)
    new_block.mining()
