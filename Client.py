import socket
import random
import time

#Endereço e porta
HOST = 'localhost'
PORT = 50000

#Função que gera um número
def gerarNum():
    return str(random.randint(1, 9999999))

#Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    #Gera um número
    data = gerarNum()
    print('Número gerado:', data)

    # Envia o número para o servidor
    s.send(data.encode())

    # Recebe a resposta do servidor
    msg = s.recv(1024).decode()
    print(msg, ' FIM')

    # Pausa por 10 segundos
    time.sleep(10)

# Fecha a conexão
s.close()
