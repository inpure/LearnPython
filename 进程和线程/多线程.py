# Python的threading模块有个current_thread()函数，
# 它永远返回当前线程的实例。主线程实例的名字叫MainThread，
# 子线程的名字在创建时指定，名字仅仅在打印时用来显示，完全没有其他意义，
# 如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
import os
import time, threading


# 线程执行函数
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    print(f'当前进程是：{os.getpid()}') # 查看进程id
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
print(f'当前进程是：{os.getpid()}')
t = threading.Thread(target=loop, name='LoopThread')  # 创建线程
t.start()  # 启动线程
t.join()  # join()方法等待线程结束后再继续往下运行
print('thread %s ended.' % threading.current_thread().name)