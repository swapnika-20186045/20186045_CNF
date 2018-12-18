import socket
def main():
	host = '10.10.9.37'
	port = 3211
	s = socket.socket()
	s.connect((host, port))

	message = input("enter text: ")
	while message != 'q':
		s.send(message.encode())
		data = s.recv(1024)
		print("Received from server: " + str(data.decode()))
		message = input("received")
	s.close()
if __name__ == '__main__':
	main()