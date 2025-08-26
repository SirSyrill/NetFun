#import socket module
from socket import *
import sys
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverPort = 6789  # note: this can be changed if needed
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print(f"Listening on http://localhost:{serverPort}")
while True:
#Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()           
    try:
        message = connectionSocket.recv(1024).decode() 
        print("receive request :/n", message)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode()) #was missing content type and another set opf \r\n at the end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())

        #Close client socket
        connectionSocket.close()
    ##break  <--- if we want a singe connection
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
