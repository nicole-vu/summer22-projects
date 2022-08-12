import socket
from _thread import *
import sys

server = "192.168.0.5"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port)) # binds the IP address to the port
except socket.error as e:
    str(e)

s.listen(2) # listens to a connection for 2 people
print("Waiting for connection, Server Started")

# FUNCTIONS
def threaded_client(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)
            
            conn.sendall(str.encode(reply))
        except:
            break


while True:
    conn, addr = s.accept() # accept incoming connection
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))