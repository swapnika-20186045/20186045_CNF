import socket
import threading
import os, signal

s = socket.socket()
def main():
    host = '10.10.9.37'
    port = 4500
    
    s.connect((host, port))
    msg = s.recv(1024).decode()
    print(msg)
    s.send(input().encode())
    threading.Thread(target = client, args = ()).start()
    
    while True:
        msg = s.recv(1024).decode()
        print(msg)
        if msg == "You have exited the chat!! ":
            os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
    s.close()

def client():
    while True:
        msg = input("Your msg: ")
        s.send(msg.encode())
    s.close()

if __name__ == '__main__':
    main()