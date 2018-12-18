import socket
def main():
    host = '10.10.9.37'
    port = 4010

    server = ('10.10.9.37', 4000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = input("enter text: ")
    while message != 'q':
        s.sendto(message.encode(), server)
        data = s.recv(1024)
        print("Received from server: " + str(data.decode()))
        message = input("received")
    s.close()

if __name__ == '__main__':
    main()