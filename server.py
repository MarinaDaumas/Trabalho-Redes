from socket import *

notas = {119050872: {"T1": 8.8, "T2": 9.0}, 119048468: {"T1": 8.2, "T2": 9.1}, 112948927: {"T1": 8.8, "T2": 9.0}, 118048725: {"T1": 8.8, "T2": 9.0}}


serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("127.0.0.1",serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
while 1:
    connectionSocket, addr = serverSocket.accept()
    matricula = int(connectionSocket.recv(1024).decode('UTF-8'))
    print(matricula)
    t1, t2 = "T1: " + str(notas[matricula]["T1"]), "T2: " + str(notas[matricula]["T2"])
    connectionSocket.send(t1.encode())
    connectionSocket.send(t2.encode())

    connectionSocket.close()
