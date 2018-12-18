import socket

def main():
    host = '10.10.9.37'
    port = 1000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c,addr = s.accept()
    print("Connection from : " + str(addr))

    while True:
        data = c.recv(1024)
        data = data.decode()
        print("from connected user: " + str(data))
        data = str(data)
        cvrt = conversion(data)
        print("Sending data: " + str(cvrt))
        c.send(str(cvrt).encode())
    c.close()

def conversion(data) :
    lst = data.split(" ")
    if(lst[1] == "INR"):
        c = int(lst[2]) / 67

    if(lst[1] == "Yen") :
        c = int(lst[2]) / 113.47

    if(lst[1] == "Pounds") :
        c = int(lst[2]) / 0.75

    if(lst[1] == "Dollars") :
        if(lst[4] == "INR"):
            c = int(lst[2]) * 67
        if(lst[4] == "Yen") :
            c = int(lst[2]) * 113.47
        if(lst[4] == "Pounds") :
            c = int(lst[2]) * 0.75
    return c

if __name__ == '__main__':
    main()
