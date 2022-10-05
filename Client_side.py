import socket
import time
HEADER = 64
PORT = 5003
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "10.15.39.218"
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
while msg.upper() != "Q":
    msg = input(f"""press enter to update messages
    Type a message here: """)
    send(msg)
    time.sleep(0.1)

send(DISCONNECT_MESSAGE)