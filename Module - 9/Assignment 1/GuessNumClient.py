import socket

def main():
	host = '10.10.9.37'
	port = 4050
	s = socket.socket()
	s.connect((host, port))
	print(s.recv(1024).decode())
	
	message = input("enter text: ")
	while message != 'q':
		s.send(message.encode())
		data = s.recv(1024)
		print("Received from server: " + str(data.decode()))
		temp = data.decode().split()
		if(temp[0] == 'Bingo!!'):
			break
		message = input("Input: ")
	# print("Client Closed")
	s.close()

if __name__ == '__main__':
	main()
