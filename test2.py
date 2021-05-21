
import socket
import threading
import sys
import signal


# AF_INET: IPV4, SOCK_STREAM: TCP
client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))         # connect localhost:8000


def receive_():
    while True:
        ge_data = client.recv(1024)
        
        # 测试得到结果 服务端按了ctrl c  这里无限收到消息长度为0 主动终止该线程
        if len(ge_data) == 0:
            print('服务端按了ctrl c 关闭收消息线程')
            # 直接泡异常 终止主线程
            # raise RuntimeError('终止主线程')

            break
        
        print('接收到的消息:%s' % ge_data.decode('UTF-8'))


def send_():
    while True:
        try:
            send_data = input('请输入发送的消息:')
            # 向客服发送消息
            client.send(send_data.encode('UTF-8'))
            if send_data == 'quit':
                client.close()             # close connection
                break
        except Exception as err:
            break


# 成功建立连接后 开启 收消息和发送消息的线程
# 一直监听消息的线程
# 子线程的daemon属性为True，主线程运行结束时不对这个子线程进行检查而直接退出，同时所有daemon值为True的子线程将随主线程一起结束，而不论是否运行完成
receive_thread = threading.Thread(target=receive_)
receive_thread.daemon = True
receive_thread.start()

# 发送消息的线程
send_thread = threading.Thread(target=send_)
send_thread.daemon = True
send_thread.start()


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    # client.close()
    # stop_thread()
    sys.exit(0)


# 监听ctrl c 主动中断脚本
signal.signal(signal.SIGINT, signal_handler)
while receive_thread.is_alive() and send_thread.is_alive():
    pass
