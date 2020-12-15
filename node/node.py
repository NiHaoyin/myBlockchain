import threading
import time
from block.block import block

class node(threading.Thread):
    def __init__(self, node_id):
        self.node_id = node_id
        super().__init__()
        print("Node ", self.node_id, " is initialized")
        

    def run(self):
        current_block = block()
        current_block.mining()
        
if __name__ =="__main__":
    nodes_num = 10
    nodes = list()
    for i in range (0, nodes_num):
        nodes.append(node(i))
    for n in nodes:
        n.start()
        # n.run()
