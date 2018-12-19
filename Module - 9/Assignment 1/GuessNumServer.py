import socket
import random
import threading

def main():
    host = '10.10.9.37'
    port = 4050

    s = socket.socket()
    s.bind((host, port))

    s.listen(10)

    while True:    
        c,addr = s.accept()
        print("Connection from: " + str(addr))
        c.send("Welcome to the Game!! Guess any number".encode())
        threading.Thread(target = GuessNum, args = (c,addr)).start()

def GuessNum(c, addr) :
    connection = True
    n = random.randint(1, 101)
    while connection:
        data = c.recv(1024).decode()
        if data == "q":
            break
        data = int(data)
        if data == n:
            c.send("Bingo!! You Guessed correct".encode())
            connection = False
        elif data < n and data >= 0:
            c.send("Input is less than guess number".encode())
        elif data > n and data <=100:
            c.send("Input is greater than guess number".encode())
        else:
            c.send("Input is invalid".encode())
    print("server closed from" + str(addr))
    c.close()

if __name__ == '__main__':
    main()
