#import socket module
from socket import *
import sys
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket

#Fill in start
serverPort = 6789  # note: this can be changed if needed
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print(f"Listening on http://localhost:{serverPort}")
#Fill in end

while True:
#Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()      #Fill in start   #Fill in end     
    try:
        message = connectionSocket.recv(1024).decode()  #Fill in start   #Fill in end
        print("receive request :/n", message)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() #Fill in start   #Fill in end  

        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode()) #was missing content type and another set opf \r\n at the end
        #Fill in end


        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())
        #Fill in end

        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
