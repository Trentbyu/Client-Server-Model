# Overview

In this softwarre i show how to prefrom a clinet based server.To opreate the client based server you will need either the ip address or the local ip address for you computer on your networl. This has to be the same on the client and the sever for them to be able to connect to each other. This can be done by changing the code for the SERVER varible at the start of both the cleint and the server code file. 
<br>
<br>
This program was written to show a model for the client based system. This software thaught me more about threads and how a server can use threads to handle more than one clinet at a time. I was able to model this in python and get a better understanding of networking. 
<br>
<br>
[Software Demo Video](http://youtube.link.goes.here)

# Network Communication


Client-server is a relationship in which one program (the client) requests a service or resource from another program (the server)
<br>
This sever uses UDP and data and be sent or recived when ever. The port number is 5003 altough it can be 5000 - 50005 and other ones as well altiough those are what i used.
<br>
The format for messages are that the cline can send any things to the sever and it be displayed to the sever. The sever can then send the messages back the clients so they can see and reply to the messages.

# Development Environment

The tools i used to devolop this software was VS code
<br>
I used python langauge to write this code. The modules i used were pysimplegui, sockets, and threading.
# Useful Websites


* [docs.python.org](https://docs.python.org/3/library/socket.html)
* [Geeks for Geeks](https://www.geeksforgeeks.org/socket-programming-python/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Add instent refresh for the clinet 
* Be able to send pickled information with the pickle module 
* Have more functions than just messages
