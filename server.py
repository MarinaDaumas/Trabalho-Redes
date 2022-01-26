from socket import *

notas = {1: {"T1": 8.8, "T2": 9.0}, 2: {"T1": 8.2, "T2": 9.1}, 3: {"T1": 8.5, "T2": 9.2}, 4: {"T1": 7, "T2": 9.0} ,5: {"T1": 5, "T2": 7}, 6: {"T1": 7, "T2": 9}, 7: {"T1": 8.7, "T2": 9.0}, 8: {"T1": 8.8, "T2": 9.0}, 9: {"T1": 5.7, "T2": 9.0}, 10: {"T1": 8.8, "T2": 9.0},11: {"T1": 7.7, "T2": 9.0},
12: {"T1": 8.8, "T2": 8}, 13: {"T1": 10, "T2": 9.1}, 14: {"T1": 5, "T2": 6}, 15: {"T1": 7, "T2": 9.0} ,16: {"T1": 8.8, "T2": 9.9}, 17: {"T1": 8.7, "T2": 9.3}, 18: {"T1": 7, "T2": 8}, 19: {"T1": 8.8, "T2": 7}, 20: {"T1": 7, "T2": 7}, 21: {"T1": 6.8, "T2": 9.0},22: {"T1": 7.8, "T2": 9.0},  }


serverPort = 12000 #porta 
serverSocket = socket(AF_INET,SOCK_STREAM) # criação do socket, stream: fica ouvindo continuamente
serverSocket.bind(("127.0.0.1",serverPort)) # se conecta a porta
serverSocket.listen(1) # ouve de 1 em 1 segundo
# serverSocket.settimeout()

print ("The server is ready to receive") #welcome socket?

connectionSocket, addr = serverSocket.accept()
pkt_0 = connectionSocket.recv(1024)
connectionSocket.send(pkt_0)
    
while True:      
    matricula = connectionSocket.recv(1024) #pega o que vem do socket
    connectionSocket.send(matricula)
    x = connectionSocket.recv(1024)

    while x.decode('UTF-8') != "ok":
        matricula = x
        connectionSocket.send(matricula)
        x = connectionSocket.recv(1024)

    matricula = int(matricula.decode('UTF-8'))

    try:
        resultado_notas = "Nota T1: " + str(notas[matricula]["T1"]) + " Nota T2: " + str(notas[matricula]["T2"]) #le no dicionario se essa matricula está lá e pega

    except:
        resultado_notas = "Matricula não cadastrada"
        
    connectionSocket.send(resultado_notas.encode()) #retorna a mudanca
    
    # else:
    #     matricula = int(connectionSocket.recv(1024).decode('UTF-8')) #pega o que vem do socket
    #     connectionSocket.send(matricula)

connectionSocket.close() #fecha 

    
