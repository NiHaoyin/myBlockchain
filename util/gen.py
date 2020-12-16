from hashlib import sha256
import random
import sys


# generate random Transaction Root
def gen_tx_root():
    tx_root = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba',8))  # generate 256-character-long string
    # print("original tx_root is:", tx_root)
    s = sha256()  # Get the hash algorithm.
    s.update(tx_root.encode("utf-8"))  # Hash the data.
    hash_value = s.hexdigest()  # Get the hash value.
    return hash_value


# generate random 4-byte-long nonce
def gen_nonce():
    return str(random.randint(0, sys.maxsize))


if __name__ == '__main__':
    print("hashed tx_root is:", gen_tx_root())