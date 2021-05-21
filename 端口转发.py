import socket


s = socket.socket()
#本机ip地址和端口
host = '127.0.0.1'
port = 10022
#远端ip地址和端口
host2 = '127.0.0.1'
port2 = 9090

s.bind((host,port))
print('本机ip地址和端口'+host+':'+str(port))
print('远端ip地址和端口'+host2+':'+str(port2))

s.listen(5)

while True:
    print('等待连接')
    c,addr = s.accept()
    recv_data = c.recv(1024)
    print('收到'+host+':'+str(port)+'的数据:')
    print(recv_data)
    
    s2=socket.socket()
    s2.connect((host2, port2))
    
    print('转发到'+host2+':'+str(port2)+'的数据:')
    print(recv_data)
    s2.sendall(recv_data)
    
    accept_data = s2.recv(1024)
    print('转发收到'+host2+':'+str(port2)+'的数据:')
    print(accept_data)
    
    s2.close()
    
    print('转发回'+host+':'+str(port)+'的数据:')
    print(accept_data)
    
    c.sendall(accept_data)
    c.close()
    
