# 用队列 Queue 进行进程间通讯
import os
import time
import random
from multiprocessing import Process, Queue


def write(q:Queue):
    print(f'写进程开始运行，id 是：{os.getpid()}')
    for v in 'ABCDE':
        print(f'将数据 {v} 放入队列')
        q.put(v)
        time.sleep(random.random()*2)


def read(q:Queue):
    print(f'读进程开始运行，id 是：{os.getpid()}')
    while True:
        v = q.get(True)
        print(f'从队列得到数据 {v}')


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()