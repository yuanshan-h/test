# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 22:55:04 2021

@author: 22943
"""
#server
import socket
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = socket.gethostname()
port = 12345
server.bind((host,port))
for i in range(0,10):
	mes,addr = server.recvfrom(1024)
	mes1 = mes.decode()
	backfeed="连接成功" 
	print(mes1)
	if (i%2==0):    #   服务器进行回应
		server.sendto(backfeed.encode(),addr)
	else:         #   服务器不回应
		continue
server.close()

'''

#client
import socket
import time

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # 创建套接字
host = socket.gethostname()
client.settimeout(1) #  设置连接超时值
for i in range(0,10):
	mes = "请求连接"
	sendtime=time.time()
	client.sendto(mes.encode(),(host,12345))
	try:     # 收到服务器的回应
		mes2,addr= client.recvfrom(1024)
		backfeed = mes2
		RTT = time.time()-sendtime  #  计算往返时延    
		print(backfeed.decode()+'     RTT = %.6f'%(RTT))
	except Exception:   #  当服务器没有回应时
		print("连接超时")	   
client.close()
   