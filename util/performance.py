import sys
import logging

mining_time_list = list()

# key: node id  value: the number of blocks the node digs out
miner_account = dict()


def test_growth_rate():
    total_mining_time = 0
    max_mining_time = -1
    min_mining_time = sys.maxsize
    for m in mining_time_list:
        total_mining_time = total_mining_time+m
        if m > max_mining_time:
            max_mining_time = m
        if m < min_mining_time:
            min_mining_time = m
    average_mining_time = total_mining_time/(len(mining_time_list)-1)
    logging.info("average mining time is: %d" % average_mining_time)
    logging.info("maximum mining time is: %d" % max_mining_time)
    logging.info("minimum mining time is: %d" % min_mining_time)


def print_miner_account():
    logging.info("The miner account is:")
    logging.info(miner_account)


def get_evil_node_block(honest_node_num):
    evil_miner_blocks = list()
    for miner in miner_account:
        if miner > honest_node_num:
            evil_miner_blocks.append(miner_account[miner])
    total_evil_blocks = 0
    for b in evil_miner_blocks:
        total_evil_blocks = total_evil_blocks+b
    return total_evil_blocks
