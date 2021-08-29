import os
import random
import time
from multiprocessing import Process


def run_process(name):
    print(f'运行子进程 {name} ，进程id是:{os.getpid()}')
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('进程 %s 运行了 %.2f s' % (name, (end-start)))


if __name__ == '__main__':
    print(f'父进程的id是：{os.getpid()}')
    p = Process(target=run_process, args=('test',))  # 创建一个Process实例
    print('子进程即将运行')
    p.start()
    p.join()
    print('子进程运行结束')
