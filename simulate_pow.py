import threading
from chain.chain import block_chain
import logging
from util.performance import test_growth_rate, print_miner_account, get_evil_node_block
from util.log import init_log
import time

chain = block_chain()
chain.mining(-1)
evil_chain = block_chain()

# attackers attack the first block
evil_chain.chain[0].hack()
hack_flag = False


def mining(node_id):
    logging.info("honest node %d is ready." % node_id)
    for j in range(0, 20):
        chain.mining(node_id)


def attacking(node_id):
    global chain, hack_flag
    logging.info("evil node %d is ready." % node_id)
    for j in range(0, 20):
        if hack_flag:
            chain.mining(node_id)
        else:
            evil_chain.mining(node_id)  # other evil nodes haven't hacked the blockchain
            if evil_chain.length() > chain.length() and hack_flag is False:
                chain = evil_chain
                hack_flag = True
                logging.info("Attackers hack the chain at block num %d." % (evil_chain.length()-1))
                logging.info("EVIL CHAIN WINS.")


def simulate_pow(honest_node_num=10, evil_node_num=0, difficulty="00000"):
    nodes = list()
    chain.set_difficulty(difficulty)

    # initiate honest nodes
    for i in range(1, honest_node_num):
        nodes.append(threading.Thread(target=mining, args=(i,)))
    # initiate evil nodes
    for i in range(honest_node_num, honest_node_num+evil_node_num):
        nodes.append(threading.Thread(target=attacking, args=(i,)))

    i = 1
    # start honest nodes
    for n in nodes:
        n.start()
        logging.info("node %d starts mining." % (i+1))
        i = i + 1

    for n in nodes:
        n.join()

    if chain.check():
        chain.print()
        logging.info("block chain length is: %d", chain.length())
        logging.info("total evil blocks is: %d" % get_evil_node_block(honest_node_num))

        test_growth_rate()
        print_miner_account()
    else:
        logging.warning("THE BLOCK CHAIN IS NOT VALID.")


if __name__ == "__main__":
    init_log(honest_node_num=15, evil_node_num=0, difficulty="0000")
    simulate_pow(honest_node_num=15, evil_node_num=0, difficulty="0000")  # change the arguments
