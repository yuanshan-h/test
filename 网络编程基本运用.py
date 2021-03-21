# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 16:46:23 2021

@author: 22943
"""
'''
# server
import socket #导入模块
server = socket.socket()    #建立一个服务端
host = socket.gethostname()   #获取主机ip地址
port = 12345    #设置端口
server.bind((host,port))    #绑定端口
server.listen(5)     #等待连接
while True:
   c,addr = server.accept()     #建立连接
   feedback = c.recv(1024)     #接受服务端发送的信息
   print(feedback.decode())     #打印接受到的信息
   message = input("请输入要发送的信息：")
   c.send(message.encode("utf-8"))      #发送信息
   c.close()       #关闭服务端
 '''
 #client
import socket
client =socket.socket()
host = socket.gethostname()
port = 12345

client.connect((host,port))     #建立连接
message="连接成功"
client.send(message.encode("utf-8"))    #发送信息 并将信息编译成python3能读懂的biye流
print(client.recv(1024).decode())   #解码收到的信息并打印出来
client.close()