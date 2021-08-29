import threading

# 假定这是你的银行存款:
balance = 0


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(2000000):
        # 获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 改完释放锁
            lock.release()


if __name__ == '__main__':
    lock = threading.Lock()  # 创建锁。如果没有锁，balance 结果不一定为 0
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
