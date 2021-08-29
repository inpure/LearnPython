import os
import random
import time
from multiprocessing import Pool


def run_process(name):
    print(f'运行子进程 {name} ，进程id是:{os.getpid()}')
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('进程 %s 运行了 %.2f s' % (name, (end-start)))


if __name__ == '__main__':
    print(f'父进程id是：{os.getpid()}')
    p = Pool(8)     # 进程池
    print('即将运行子进程')
    for i in range(8):
        p.apply_async(run_process, args=(i,))
    p.close()   # 调用join()之前必须先调用close()
    p.join()    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('所有子进程结束')