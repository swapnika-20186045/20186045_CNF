import socket
def main():
	host = '10.10.9.37'
	port = 3211

	s = socket.socket()
	s.bind((host, port))

	s.listen(1)
	c, addr = s.accept()
	while True:
		data = c.recv(1024)
		if not data:
			break
		print ("received data: " + str(data.decode()))
		data = str(data.decode()).upper()
		print ("sending: " + str(data))
		c.send(data.encode())
	c.close()

if __name__ == '__main__':
	main()