from AKCN import *
import os

serverPort = 12000

# 1. Create a UDP socket (SOCK_DGRAM)
serverSocket = socket(AF_INET, SOCK_DGRAM)

# 2. Bind the socket to the server port
serverSocket.bind(("127.0.0.1", serverPort))
print("The server is ready to receive")

# 3. Infinite loop to process requests
while True:
    # Receive the requested filename and the client's address details
    data, clientAddress = serverSocket.recvfrom(2048)
    filename = data.decode("utf-8")
    print(f"Received request for file: {filename} from {clientAddress}")
    
    # 4. Try opening the requested file
    try:
        file = open(filename, "r")
        l = file.read(2048) # Read up to 2048 bytes
        file.close()
    except FileNotFoundError:
        l = "Error: File not found on the server."

    # 5. Send the file content (or error message) back to the client
    serverSocket.sendto(bytes(l, "utf-8"), clientAddress)
    print("Sent back to client:\n", l)