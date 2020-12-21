from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)

addr = ("127.0.0.1", 8888)
tcp_socket.connect(addr)
while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket.send(msg.encode())
    # if msg == "##":
    #     break
    data = tcp_socket.recv(1024)
    print("服务端返回信息为：", data.decode())

tcp_socket.close()