# Programacao-de-sockets
Este é um trabalho simples, introdutório, apenas para permitir um primeiro contato com a programação em sockets. Neste trabalho iremos desenvolver duas aplicações. Uma aplicação cliente que se conecta a um servidor e uma aplicação servidor.


# Descrição

## Programa Cliente
- Primeiramente o endereço do servidor e a porta são definidos, HOST e PORT respectivamente.
- Após isso vai gerar um número usando a função 'gerarNum' que gera um número aleatório de até 30 casas utilizando a função random que define um intervalo adicionando um valor mínimo e um valor máximo.
- Então é criado um objeto 's' e passar os parâmetros AF_INET e SOCK_STREAM que vão definir o objeto como IPv4 4 e TCP.
- Definido o objeto ele se conectar com o servidor que foi definido por HOST e PORT usando a função connect(). 
- Após a conexão com o servidor, irá entrar em um loop uma vez que a condição de while for cumprida, assim continuará adicionando um valor aleatório em 'data'. 
- Em seguida envia para o servidor com o método send(), mas em forma de string por causa do método encode(). 
- Depois do valor ser enviando o cliente recebe a resposta do servidor com o método recv() e a mensagem e decodificada usando o método decode() para que possa ser lida como uma string e finalmente imprimir a mensagem recebida junto com a mensagem ' FIM'.
- Então repete a cada 10 segundos definido pelo time.sleep(10)
- Por fim a conexão é encerrada com o método close()

## Programa Servidor
- Assim como no cliente, primeiramente foi definido o endereço do servidor e a porta HOST e PORT.
- Logo em seguida o objeto 's' será criado usando AF_INET e SOCK_STREAM, IPv4 e TCP respectivamente.
- Em seguida o método bind() é utilizado para associar o objeto 's' ao endereço e porta definidos em HOST e PORT.
- Após isso o servidor começa a esperar pela conxão utilizando o método listen().
- Enquanto aguarda a conexão 'conn' e 'ender' vão receber o método accept() do objeto 's', que vai bloquear a execução até que um cliente se conecte.
- Depois que houver uma conexão o servidor vai receber um valor utilizando o método recv() do objeto 'conn' e vai decodificar utilizando o método decode() para poder ser lido como uma string.
- Após receber o número decodificado, o servidor verifica o tamanho dele utilizando a função len().
- Tendo verificado o tamanho do número o servidor cria uma condição usando if onde caso a quantidade de digitos do número for menor que 10 ele irá ser inserido em uma segunda condição onde %2==0 ou se o resto da divisão for igual a zero então o número é par e será atribuido a string 'PAR' e se o resto for igual a 1, então será atribuido a string 'IMPAR'.
- Caso a condição não seja atendida o else é ativado e o número será retornado em forma de string.
- Finalizando o processo o servidor enviará a resposta ao cliente utilizando o método send() do objeto 'conn' sendo codificada como uma string com o método encode().
