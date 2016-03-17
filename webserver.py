# Import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a server socket, use port 6789
# Fill in start
serverSocket.bind(('',6789))
serverSocket.listen(1)
# Fill in end
while True:
    # Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Send the HTTP status line and HTTP headers Content-Length and Content-Type into socket
        # Fill in start
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
        connectionSocket.send(outputdata)
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            # Fill in start
            connectionSocket.send(outputdata[i])
            # Fill in end
        connectionSocket.close()
    except IOError:
        # Send the HTTP status line for file not found
        # Fill in start
        connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
        # Fill in end
        connectionSocket.send("<!DOCTYPE html><html><head><title>404 Not Found</title></head><body>404 Not Found</body></html>\r\n")
        connectionSocket.close()
serverSocket.close()
