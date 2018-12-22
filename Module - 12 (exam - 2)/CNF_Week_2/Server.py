import socket
import threading
import collections

s = socket.socket()
dict_of_rollnumbers = {}
clients_list = []
def main():
	host  = '10.10.9.37'
	port = 2500

	s.bind((host,port))
	s.listen(10)

	file = open("data.csv", "r")
	data = []
	for i in file:
	    data.append(i)

	for j in data:
	    words = j.split(",")
	    dict_of_rollnumbers[words[0]] = [words[1], words[-1].rstrip('\n')]

	while True:
	    c, addr = s.accept()
	    print ('connection established from : '+ str(addr))
	    c.send("Welcome to mark Attendence ".encode())
	    if (c not in clients_list):
	        clients_list.append(c)
	        threading.Thread(target = Connection, args = (c,)).start()
	s.close()

def Connection(c):
    while True:
        msg = c.recv(1024).decode()
        print(msg)
        word = msg.split(" ")
        for c in clients_list:
            if word[0] == 'mark':
                num = dict_of_rollnumbers.get(word[-1])
                if word[1] not in dict_of_rollnumbers:
                    c.send("Person not available".encode())
                else:
                    c.send(num[0].encode())
                    answer = c.recv(1024).decode()
                    if answer == num[-1]:
                        c.send("Attendence marked".encode())
                    else:
                        c.send("Attendence not marked".encode())

if __name__ == '__main__':
    main()
