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
            # 改完释放锁，用try...finally来确保锁一定会被释放，
            # 否则那些苦苦等待锁的线程将永远等待下去，成为死线程
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

'''锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，
坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上
只能以单线程模式执行，效率就大大地下降了。其次，由于可以存在多个锁，
不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导
致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
'''