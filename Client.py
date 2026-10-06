from socket import *

serverName = "127.0.0.1"
serverPort = 12000

# 1. Create a TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# 2. Connect to the server
clientSocket.connect((serverName, serverPort))

# 3. Get the filename from the user
sentence = input("Enter file name: ")

# 4. Send the filename to the server
clientSocket.send(sentence.encode())

# 5. Receive the file contents from the server
filecontents = clientSocket.recv(4096).decode()

# 6. Print the received contents
print('From Server:\n', filecontents)

# 7. Close the socket
clientSocket.close()
