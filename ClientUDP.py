from AKCN import *

serverName = "127.0.0.1"
serverPort = 12000

# 1. Create a UDP socket (SOCK_DGRAM)
clientSocket = socket(AF_INET, SOCK_DGRAM)

# 2. Get the filename from the user
sentence = input("Enter file name: ")

# 3. Send filename to the server
clientSocket.sendto(bytes(sentence, "utf-8"), (serverName, serverPort))

# 4. Receive file contents back from the server
filecontents, serverAddress = clientSocket.recvfrom(2048)

# 5. Decode and print the file data
print('From Server:\n', filecontents.decode("utf-8"))

# 6. Close the socket
clientSocket.close()