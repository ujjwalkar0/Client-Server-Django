from django.shortcuts import render
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.listen(5)

def home():
    clientsocket,address = s.accept()
    print(f"Connection from {address} established !")
    clientsocket.send(bytes("Welcome to the server !","utf-8"))
    clientsocket.close()
