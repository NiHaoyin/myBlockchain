import threading
from block_chain.chain import block_chain


chain = block_chain()


def mining(node_id):
    for j in range(0, 30):
        chain.mining(node_id)


def simulate_pow(nodes_num=10, difficulty="000"):
    nodes = list()
    chain.set_difficulty(difficulty)
    for i in range(0, nodes_num):
        nodes.append(threading.Thread(target=mining, args=(i,)))
    j = 0
    for n in nodes:
        n.start()
        print("node %d starts mining." % j)
        j = j+1
    for n in nodes:
        n.join()
    chain.check()
    chain.display()


if __name__ == "__main__":
    simulate_pow()
