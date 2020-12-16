from hashlib import sha256
from util.gen import gen_tx_root, gen_nonce
import time


class block:
    # a block header contains 
    # the hash value of its previous block, nonce, transaction root and time stamp
    # the difficulty of digging out a block is set to 000 by default
    def __init__(self, previous_hash, difficulty="00000", node_id=-1):
        self.previous_hash = previous_hash
        self.nonce = gen_nonce()
        self.tx_root = gen_tx_root()
        self.time_stamp = time.time()
        self.t = difficulty  # the difficulty to mine a block
        self.miner = node_id

    # return the hash value of this block
    def hash(self):
        s = sha256()
        s.update(self.previous_hash.encode("utf-8"))
        s.update(self.nonce.encode("utf-8"))
        s.update(self.tx_root.encode("utf-8"))
        s.update(str(self.time_stamp).encode("utf-8"))
        hash_value = s.hexdigest()
        return hash_value

    def check(self):
        return self.check_nonce(self.nonce)

    #  if the current hash value is less than t, return True else return False
    def check_nonce(self, nonce):
        s = sha256()
        s.update(self.previous_hash.encode("utf-8"))
        s.update(nonce.encode("utf-8"))  
        s.update(self.tx_root.encode("utf-8"))
        s.update(str(self.time_stamp).encode("utf-8"))
        hash_value = s.hexdigest()
        return hash_value.startswith(self.t)

    def display(self):
        print("previous hash is:", self.previous_hash)
        print("nonce is:", self.nonce)
        print("tx_root is:", self.tx_root)
        print("time stamp is:", self.time_stamp)
        print("difficulty is:", self.t)
        print("hash value is:", self.hash())
        print("miner is:", self.miner)

    # set this block to be genesis
    def set_genesis(self):
        self.nonce = str(0)
        self.tx_root = "This is genesis."
        self.time_stamp = 1608040156.650194
        self.previous_hash = str(0)

    def hack(self):
        self.tx_root = "This block is hacked."

    # difficulty is a str starts with several zeros
    def set_difficulty(self, difficulty):
        self.t = difficulty


def gen_genesis():
    genesis_block = block(str(0))  # the previous hash value of genesis is set to 0
    genesis_block.set_genesis()
    return genesis_block


if __name__ == "__main__":
    s = sha256()
    s.update("hello world".encode("utf-8"))
    initial_hash = s.hexdigest()
    new_block = block(initial_hash)

