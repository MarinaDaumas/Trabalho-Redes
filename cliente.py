from socket import *

serverName = "127.0.0.1" #endereço de IP do servidor
serverPort = 12000 # numero da porta que o servidor está

#indica o processo que esta rodado no outro hospedeiro?
clientSocket = socket(AF_INET, SOCK_STREAM) #aqui mostra que é TCP, criação do socket de cliente

clientSocket.connect((serverName, serverPort)) #cria o cliente e conecta ao servidor e a porta.

# teste de conexão
connection_test = "connected".encode()
clientSocket.send(connection_test)
conectado = False
try: 
	clientSocket.recv(1024)
	conectado = True
except:
	print("Erro de conexão.")
	clientSocket.close()#testou se conecttou

if conectado:
	matricula = input("Input matricula:").encode() #escreve a matricula, input

	# codifica a mensagem
	
	received = False
	while not received: #só sai do loop depois que recebe
		clientSocket.send(matricula) # matricula enviada
		try:
			clientSocket.settimeout(10) #espera no maximo 10 segundos para a resposta
			ack_0 = clientSocket.recv(1024)#recebe o codigo enviado da matricula
			if (ack_0 == matricula):
				clientSocket.send("ok".encode())#se for igual, manda ok
				received = True
			else:
				received = False

		except:
			received = False

	"""
	matricula = int(connectionSocket.recv(1024).decode('UTF-8')) #pega o que vem do socket
	connectionSocket.send(matricula)
	x = connectionSocket.recv(1024).decode('UTF-8')

	while x != "ok":
		matricula = x
		connectionSocket.send(matricula)
		x = connectionSocket.recv(1024).decode('UTF-8')


	while x == "not ok":
		x = notas
		notas = clientSocket.recv(1024)
		connectionSocket.send(notas)
		x = connectionSocket.recv(1024).decode('UTF-8')

	while x != "ok":
		matricula = x
		connectionSocket.send(matricula)
		x = connectionSocket.recv(1024).decode('UTF-8')



	received = False
	while not received:
		try: 
			clientSocket.settimeout(10)
			notas = clientSocket.recv(1024)
			clientSocket.send(notas)

		except:
			pass
    """
	notas = clientSocket.recv(1024)

	print ("From Server:", notas.decode('UTF-8'))
	
	clientSocket.close()