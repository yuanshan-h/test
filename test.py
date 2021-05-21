import socket
import threading
from datetime import datetime
import sys
host1='127.0.0.1'
port1=20202
server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind((host1, port1))              # bind to localhost:8000
server.listen()                             # listen for clients
print('server is listen 20202')
def process_client(socke, addr):
    sock = socke  # type:socket.socket

    print('收到客户端连接,地址为:{}'.format(addr))

    def receive_(sock, addr):
        while True:
            ge_data = sock.recv(1024)               # receive data
            
            # 测试得到结果 客户端按了ctrl c  这里无限收到消息长度为0 主动终止该线程
            if len(ge_data) == 0:
                print('客户端%sctrl c断开连接' % (addr,))
                sock.close()
                break
            
            ge_str = str(ge_data.decode('UTF-8'))
            print('收到客户端%s发送的消息为:%s' % (addr, ge_str))
            # quit 主动断开连接
            if ge_str == 'quit':
                print('客户端%s主动断开连接,终止连接' % (addr,))
                sock.close()
                break

            # print('处理客户端%s请求中。。。' % (addr,))

    def send_(sock, addr):
        while True:
            try:
                res_data = input('请输入回复给%s的内容:' % (addr,))
                sock.send(res_data.encode('UTF-8'))      # send byte data
            except Exception as err:
                print('send_send_send_', err)
                sock.close()
                break
    #  开启收消息线程
    receive_thread = threading.Thread(target=receive_, args=(sock, addr))
    send_thread = threading.Thread(target=send_, args=(sock, addr))

    # 开启发消息线程
    receive_thread.start()
    send_thread.start()

    # while receive_thread.is_alive() and send_thread.is_alive():
    #     pass


while True:
    # 接收到客户端的消息
    sock, addr = server.accept()
    # 开启一个线程去处理请求
    client_thread = threading.Thread(target=process_client, args=(sock, addr))
    client_thread.start()

server.close()
 


