import socket 
import threading
import time
HEADER = 64 # how many bytes are accepted 
PORT = 5003 # port number 
SERVER = "192.168.0.214" # what sever to start the connection on 
ADDR = (SERVER, PORT)
FORMAT = 'utf-8' # the encoder and decoder 
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

msg_dic = {}
msg_list = [" "]

def handle_client(conn, addr):
    # tells what computer is connected 
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True

    while connected:
        
        msg_length = conn.recv(HEADER).decode(FORMAT) # gets the length of the message
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT) # than recieves the message 
            if msg == DISCONNECT_MESSAGE:
                connected = False
            elif msg == "U": # if the cleint sneds an Upper case U it sends the last thing sent to the server
                conn.send(str(msg_list[-1]).encode(FORMAT))
            else:
                print(f"[{addr}] {msg}") # otherwise it will take the list
                msg_dic[addr] = msg
                msg_list.append([addr , msg])
                conn.send(str(msg_list[-1]).encode(FORMAT))
        
        
        
      

            
    conn.close()
        

def start(): # function to start the server 
    server.listen() # listen begins the server
    print(f"[LISTENING] Server is listening on {SERVER}")# tells the ip address
    while True:
        conn, addr = server.accept()# Accepts the connection and address
        thread = threading.Thread(target=handle_client, args=(conn, addr))# starts a ffunction for the new client on a thread
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") # tells how many computers are connected to the serber 
        



print("[STARTING] server is starting...")
start()