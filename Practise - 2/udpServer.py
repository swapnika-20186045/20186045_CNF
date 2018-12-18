import socket
def main():
	host = '10.10.9.37'
	port = 3249

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	# s.listen(1)
	# c, addr = s.accept()
	print ("Server Started!")
	while True:
		data, addr = s.recvfrom(1024)
		print("message from: " + str(addr))
		print("from connected user: " + str(data.decode()))
		data = str(data.decode()).upper()
		print ("sending: " + str(data))
		s.sendto(data.encode(), addr)
	s.close()

if __name__ == '__main__':
	main()
