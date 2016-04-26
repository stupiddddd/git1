#coding=utf-8
import socket
target_host="127.0.0.1"
target_port=4444
link=(target_host,target_port)
tcpclient=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpclient.connect(link)
while (1):
    a=input("please input your job:\r\n")
    if(a=='exit'):
        tcpclient.close
        print("your tcpclient was stopped")
        break
    else:
        tcpclient.send((a).encode())
        if ((tcpclient.recv(4096)).decode()):
            print("respose is:\n%s" %(tcpclient.recv(4096).decode()))
    
    
