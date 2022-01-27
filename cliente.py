from socket import *

serverName = "127.0.0.1" 
serverPort = 12000 

clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName, serverPort)) 
clientSocket.settimeout(2)

# teste de conexão
clientSocket.send("connected".encode())
conectado = False
try: 
	clientSocket.recv(1024)
	conectado = True
except:
	print("Erro de conexão.")

if conectado:
	matricula = input("Input matricula:").encode() 
	
	received = False
	while not received: 
		clientSocket.send(matricula) # envia a matricula até que seja recebida corretamete
		try:
			ack_0 = clientSocket.recv(1024)
			if (ack_0 == matricula):
				clientSocket.send("ok".encode()) # confirma que a matrícula foi recebida
				received = True
			else:
				received = False

		except:
			received = False
    
	clientSocket.settimeout(10) # define timeout maior para dar tempo de receber as notas caso haja erro no envio

	notas = clientSocket.recv(1024)
	clientSocket.send(notas)
	x = clientSocket.recv(1024)

	while x.decode('UTF-8') != "ok": 
		notas = x
		clientSocket.send(notas)
		x = clientSocket.recv(1024)

	notas = notas.decode('UTF-8')

	print ("From Server:", notas)
	
clientSocket.close()
