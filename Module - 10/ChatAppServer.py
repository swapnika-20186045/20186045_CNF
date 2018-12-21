import socket
from threading import *
import os
import signal
import time

list_of_clients = {}
s = socket.socket()
def main():
    host = '10.10.9.37'
    port = 4500
    
    s.bind((host, port))
    s.listen(10)
    print("Server established at: "+str(host))
    Thread(target = admin, args = ()).start()
    
    while True:
        c, addr = s.accept()
        msg = "Welcome to Chatroom!! \nPlease enter your name: "
        c.send(msg.encode())
        if c not in list_of_clients:
            list_of_clients[c] = "user"
            Thread(target = Chatroom, args = (c, "user")).start()
        else:
            c.send("Error Occured!! please try later".encode())
            list_of_clients.pop(c)
    s.close()

def Chatroom(c, UserName):
    UserName = c.recv(1024).decode()
    list_of_clients[c] = UserName
    Broadcast(c, UserName + " joined the group chat!")
    try:
        while c in list_of_clients:
            msg = c.recv(1024).decode()
            if msg == "q":
                msg = UserName + " exited"
                Broadcast(c, msg)
                c.send("You have exited the chat!!".encode())
                list_of_clients.pop(c)
                check()
                return 1
            else:
                msg = UserName + ": " + msg
                Broadcast(c,msg)
    except:
        list_of_clients.pop(c)
        c.send("Error Occured!! Please try later".encode())

def Broadcast(c, msg):
    key = list_of_clients.keys()
    print(msg)
    for conn in key:
        if c != conn:
            conn.send(msg.encode())

def Notify(msg):
    msg = "Admin: "+ msg
    keys = list_of_clients.keys()
    print(msg)
    for conn in keys:
        conn.send(msg.encode())

def check():
    if (active_count() == 5):
        Notify("Waiting to close the group chat, no member online.")
        time.sleep(10)
        os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)

def admin():
    while True:
        msg = input("Input: ")
        if not msg:
            print("Enter valid message..")
            continue
        if msg == "q":
            Notify("Server will shut down in 5 seconds! ")
            time.sleep(5)
            print("server closed")
            os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
            break
        else:
            Notify(msg)

if __name__ == '__main__':
    main()
