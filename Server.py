import socket

#Endereço e porta
HOST = 'localhost'
PORT = 50000

#Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print ('Aguardando conexão de um cliente')

#Aguardando conexão
conn, ender = s.accept()
print ('Conectado em ', ender)

while True:
    #'data' Recebe o número enviado pelo cliente
    data = conn.recv(1024).decode()

    print('Número recebido:', data)

    #Se o número de casas for menor que 10 o servidor -
    # envia se é PAR ou IMPAR 
    if(len(data)<10):
        if(int(data)%2==0):
            msg = 'PAR'
        else:
            msg = 'IMPAR'

    #Se o número tiver 10 casas ou mais o servidor retorna -
    # a string com o propio número
    else:
        msg = data

    #Envia uma resposta para o cliente
    conn.send(msg.encode())