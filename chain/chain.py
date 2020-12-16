from block.block import block, gen_genesis
from util.gen import gen_nonce
from util.performance import mining_time_list, miner_account
import time
import logging


class block_chain:
    def __init__(self, difficulty="0000"):
        self.chain = list()
        self.chain.append(gen_genesis())
        self.t = difficulty

    def length(self):
        return len(self.chain)

    def latest_block(self):
        return self.chain[-1]

    def set_difficulty(self, difficulty):
        self.t = difficulty

    def check(self):
        for i in range(1, len(self.chain)-1):
            if self.chain[i].check():
                continue
            else:
                print("WARNING: The block chain is NOT valid")
                return False
        print("The block chain is valid")
        return True

    def print(self):
        i = 1
        print("###########################################################")
        for b in self.chain:
            print("Block num %d" % i)
            i = i + 1
            b.display()
            print("###########################################################")

    def mining(self, node_id):
        start_time = time.time()  # record the time when the miner starts mining
        length = self.length()  # record the length when the miner starts mining

        new_block = block(self.latest_block().hash(), self.t, node_id)
        flag = False

        # mining until the length of the chain changes
        while True:
            if length == self.length():  # nobody digs out a new block
                nonce = gen_nonce()
                new_block.time_stamp = time.time()  # update the time stamp before one iteration
                # successfully dig out a block
                if new_block.check_nonce(nonce):
                    new_block.nonce = nonce
                    flag = True
                    break
                else:
                    continue
            else:
                if self.latest_block().check():
                    break
                else:
                    continue
        if flag:
            end_time = time.time()  # record the time when you finish mining
            mining_time = end_time - start_time
            logging.info("One block is dug out. Its mining time is: %d. "
                         "Its miner is %d. " % (mining_time, node_id))
            mining_time_list.append(mining_time)
            if miner_account.get(node_id) is None:
                miner_account[node_id] = 1
            else:
                miner_account[node_id] = miner_account[node_id] + 1
            self.chain.append(new_block)


if __name__ == "__main__":
    chain = block_chain()
    chain.mining(node_id=0)
    chain.print()
