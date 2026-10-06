from socket import *
import os

serverName = "127.0.0.1"
serverPort = 12000

# 1. Create a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# 2. Bind the socket to the port
serverSocket.bind((serverName, serverPort))

# 3. Listen for incoming connections
serverSocket.listen(1)
print("The server is ready to receive")

# 4. Loop to accept client requests
while True:
    # Accept connection from a client
    connectionSocket, addr = serverSocket.accept()
    
    # Receive the requested filename
    filename = connectionSocket.recv(1024).decode()
    print(f"Connection established. Requested file: {filename}")
    
    # 5. Check if file exists and send data
    try:
        with open(filename, 'r') as file:
            filecontents = file.read()
            connectionSocket.send(filecontents.encode())
    except FileNotFoundError:
        # Send error message if file is missing
        connectionSocket.send("Error: File not found on the server.".encode())
        
    # 6. Close the connection with the current client
    connectionSocket.close()
