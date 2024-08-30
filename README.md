Projeto de Comunicação Cliente-Servidor com Sockets

Este projeto é um simples aplicativo de comunicação cliente-servidor em Python usando sockets. Ele permite que você configure uma aplicação como um servidor que escuta por mensagens em uma porta específica ou como um cliente que envia mensagens para o servidor.

Requisitos
Python 3.x

Como usar
O script pode ser executado tanto no modo servidor quanto no modo cliente. Para escolher o modo de execução, use os argumentos da linha de comando ao iniciar o script.

Modo Servidor
Para iniciar o script no modo servidor, execute o seguinte comando:

bash
Copiar código
python teste.py --server --host <ENDEREÇO_HOST> --port <PORTA>
--server: Indica que o script deve ser executado no modo servidor.
--host: O endereço do host para o servidor escutar. O padrão é localhost.
--port: A porta na qual o servidor irá escutar. O padrão é 50000.

Modo Cliente
Para iniciar o script no modo cliente, execute o seguinte comando:

bash
Copiar código

python teste.py --host <ENDEREÇO_HOST> --port <PORTA> --msg <MENSAGEM>
--host: O endereço do host do servidor para onde enviar a mensagem. O padrão é localhost.
--port: A porta na qual o servidor está escutando. O padrão é 50000.
--msg: A mensagem a ser enviada para o servidor. O padrão é 'Hello world'.

Exemplo de Uso

Modo Servidor
bash
Copiar código
python teste.py --server --host localhost --port 50000
Modo Cliente
bash

Copiar código
python teste.py --host localhost --port 50000 --msg "Olá, servidor!"

Notas
Certifique-se de que a porta especificada não está em uso por outro serviço.
O script cliente só pode enviar mensagens para o servidor se o servidor estiver ativo e escutando na porta especificada.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias.
