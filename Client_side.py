import socket
import time
HEADER = 32
PORT = 5005
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.214"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length) 
    client.send(message)
    print(client.recv(2048).decode(FORMAT))



msg = " " 
while msg != "Q":
    msg = input("Enter your message here: ")
    input()
    send(msg)
    time.sleep(0.1)

send(DISCONNECT_MESSAGE)