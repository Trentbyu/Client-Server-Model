import socket 
import threading

HEADER = 64
PORT = 5002
SERVER = "192.168.0.214"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

msg_dic = {}
msg_list = []

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True

    while connected:
        
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            elif msg == "":
                show = "\n"
                for i in msg_list:
                    show += str(i) + "\n"
                conn.send(show.encode(FORMAT))
            else:
                print(f"[{addr}] {msg}")
                msg_dic[addr] = msg
                msg_list.append([addr , msg])
        conn.send("Msg received".encode(FORMAT))

            
    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        



print("[STARTING] server is starting...")
start()