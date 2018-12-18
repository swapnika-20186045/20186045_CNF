import socket

def main():
    host = '10.10.9.37'
    port = 4000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    # s.listen(1)
    # c, addr = s.accept()
    print ("Server Started!")
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode()
        print("from connected user: " + str(data))
        data = str(data)
        cvrt = conversion(data)
        print("Sending data: " + str(cvrt))
        s.sendto(str(cvrt).encode(),addr)
    s.close()

def conversion(data) :
    lst = data.split(" ")
    if(lst[1] == "INR"):
        output = int(lst[2]) / 67

    if(lst[1] == "Yen") :
        output = int(lst[2]) / 113.47

    if(lst[1] == "Pounds") :
        output = int(lst[2]) / 0.75

    if(lst[1] == "Dollar") :
        if(lst[4] == "INR"):
            output = int(lst[2]) * 67
        if(lst[4] == "Yen") :
            output = int(lst[2]) * 113.47
        if(lst[4] == "Pounds") :
            output = int(lst[2]) * 0.75
    return output

if __name__ == '__main__':
    main()
