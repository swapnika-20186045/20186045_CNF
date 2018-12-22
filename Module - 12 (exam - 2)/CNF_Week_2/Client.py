import socket

s = socket.socket()
def main():
    host = '10.10.9.37'
    port = 2500
    
    s.connect((host, port))
    msg = s.recv(1024).decode()
    print(msg)
    while True:
        s.send(input().encode())
        question = s.recv(1024).decode()
        print(question)

if __name__ == '__main__':
    main()

