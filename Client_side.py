import socket
import PySimpleGUI as sg
import time
HEADER = 64 # how many bytes 
PORT = 5003 # port number 
FORMAT = 'utf-8' # encoeer and decoder 
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.214" # The sever to connect to
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect(ADDR)

def send(msg): # function to send a message 
    message = msg.encode(FORMAT) # tells the server how big the message will be 
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT) # send the message 
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length) # sends the lenght 
    client.send(message)# sends the acutal message 
  



l = [" "] 
# this is what you see on the rigt side of the porgram
element1 =  [sg.Text("Enter here", size=(20,10))],[sg.Input(key='-INPUT-')], [sg.Button('send', key="-SEND-"),sg.Button('Quit')] , [ sg.Button("Refresh", key='-REFRESH-') ]

# this is what you see on the right side of the program
column1 = [
    [sg.Listbox(l, size=(70, 10) ,key='list')]
   

]
# this is the layout set up for the pysimplegui

layout = [
    [
        sg.Column(column1),
        sg.VSeperator(), # this puts a line down the middle of the page 
        sg.Column(element1)
    ]
]

# Create the window
window = sg.Window('MESSAGER', layout)

# Display and interact with the Window using an Event Loop

while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    if event == '-REFRESH-':
        send("U")
    if event == "-SEND-":
        send(str(values['-INPUT-']))

    sever = client.recv(4096).decode(FORMAT) # varible to hold sever info coming in 
    
    if sever != l[-1]:
        # only adds to the list if and only if it is not the same thing that was just sent. 
        l.append(str(sever))
    #updates the window with the l list 
    window['list'].update(l)


  
 


    

# Finish up by removing from the screen
window.close()
send(DISCONNECT_MESSAGE)