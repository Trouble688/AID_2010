import multiprocessing
from time import sleep


# 进程执行函数
def fun():
    print("开始运行一个进程")
    sleep(2)
    print("完成进程结束了")


# 实例化进程对象
p = multiprocessing.Process(target=fun)

# 启动进程  此刻产生进程，运行fun函数
p.start()

# 阻塞等待回收进程
p.join()