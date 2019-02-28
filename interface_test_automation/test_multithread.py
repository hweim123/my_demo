# -*- coding: utf-8


import threading
from datetime import *


def test():
    print(datetime.now())


def looptest():
    for i in range(20):
        test()


def thd():
    Threads = []
    for i in range(25):
        t = threading.Thread(target=looptest)
        Threads.append(t)
        t.setDaemon(True)
    for t in Threads:
        t.start()


if __name__ == "__main__":
    thd()
