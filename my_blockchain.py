import threading 
import time
from block.block import block


class Node(threading.Thread):
    def __init__(self, para='hi', sleep=3):
        super().__init__()
        self.para = para
        self.sleep = sleep

    def run(self):
        """线程内容"""
        time.sleep(self.sleep)
        print(self.para)


def main():
    # 创建线程
    thread_hi = Node()
    thread_hello = Node('hello', 1)
    # 启动线程
    thread_hi.start()
    thread_hello.start()
    print('Main thread has ended!')


if __name__ == '__main__':
    main()