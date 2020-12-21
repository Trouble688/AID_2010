"""
    IO并发模型 基于poll方法 tcp
"""
from socket import *
from select import *

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

# 创建tcp套接字连接客户端，处理请求
tcp_sock = socket()
tcp_sock.bind(ADDR)
tcp_sock.listen(5)

# 设置套接字连接非阻塞IO
tcp_sock.setblocking(False)

p = poll()
p.register(tcp_sock, POLLIN)
map = {tcp_sock.fileno(): tcp_sock}
# 循环的监控发生的IO事件
while True:
    events = p.poll()
    # 遍历就绪的IO对象
    for r, w in events:
        if r == tcp_sock.fileno():
            # 处理客户端连接
            connfd, addr = map[r].accept()
            print("Connect from:", addr)
            # 添加客户端连接套接字到监控列表
            connfd.setblocking(False)
            map[connfd.fileno()] = connfd
            p.register(connfd,POLLIN)
            # rlist.append(connfd)
        else:
            # 处理一个客户端的消息
            data = map[r].recv(1024)
            if not data:
                p.unregister(r)
                map[r].close()
                del map[r]
                continue
            print(data.decode())
            map[r].send(b"OK")
