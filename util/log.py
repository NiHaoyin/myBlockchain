import logging
import os


def init_log(honest_node_num, evil_node_num, difficulty):
    log_path = "honest=" + str(honest_node_num) + \
               " evil=" + str(evil_node_num) + \
               " difficulty=" + str(difficulty) + \
               ".log"
    if log_path in os.listdir("log"):
        log_path = "log/" + log_path
        os.remove(log_path)
    else:
        log_path = "log/" + log_path

    LOG_FORMAT = "%(asctime)s: %(message)s"
    DATE_FORMAT = "%H:%M:%S %p"
    logging.basicConfig(filename=log_path, level=logging.DEBUG,
                        format=LOG_FORMAT, datefmt=DATE_FORMAT)
