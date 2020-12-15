import socket 
import threading 

PORT = 5555
SERVER = "127.0.0.1"
ADDRESS = (SERVER, PORT) 
FORMAT = "utf-8"

# Client names connected to the server 
clients, names = [], [] 

# Create a new socket for server 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

server.bind(("127.0.0.1",PORT)) 

def startChat(): 
	
	print("\nServer IP : " + SERVER) 
	server.listen(2) 
	
	while True: 
		
		# accept connections and returns 
		conn, addr = server.accept() 
		conn.send("NAME".encode(FORMAT)) 
		name = conn.recv(1024).decode(FORMAT) 
		names.append(name) 
		clients.append(conn) 
		
		print(f"Name of Client : {name}") 
		
		# broadcast message 
		broadcastMessage(f"{name} joined the chat...".encode(FORMAT)) 
		
		conn.send('Connection successful...'.encode(FORMAT)) 
		thread = threading.Thread(target = handle, args = (conn, addr)) 
		thread.start() 
		
		# no. of clients connected to the server 
		print(f"Active clients : {threading.activeCount()-1}") 

# incoming messages 
def handle(conn, addr): 
	
	print(f"New connection at {addr}") 
	connected = True
	
	while connected: 
		message = conn.recv(1024) 
		broadcastMessage(message) 
	 
	conn.close() 

def broadcastMessage(message): 
	for client in clients: 
		client.send(message) 

startChat()