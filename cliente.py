from socket import *
serverName = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input("Input matricula:").encode()
clientSocket.send(sentence)

nota1 = clientSocket.recv(1024)
nota2 = clientSocket.recv(1024)
print ("From Server:", nota1.decode('UTF-8'), " ", nota2.decode('UTF-8'))
clientSocket.close()