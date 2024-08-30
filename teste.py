import argparse
import socket #mais próxima do SO

parser = argparse.ArgumentParser()

parser.add_argument('--server', action='store_true', help='para indicar aplicação com o servidor')
parser.add_argument('--host', default='localhost')
parser.add_argument('--port',default=50000)
parser.add_argument('--msg',default='Hello world',help='a mensagem a ser enviada (ignorada do servidor)')

args = parser.parse_args()

HOST = args.host
PORT = args.port
MSG = args.msg

if args.server:
    with socket.socket() as s:
        s.bind((HOST,PORT))#2
        s.listen(1)#simboliza um servidor
        conn, addr = s.accept() #handler tratamento de conexão
        with conn:
            print('Connected by',addr)
            while True:
                data = conn.recv(152)
                if not data: break
                rstr = str(data, 'utf-8')
                conn.sendall(bytearray(rstr.upper(), 'utf-8'))
else:
    with socket.socket() as s:
        s.connect((HOST, PORT))
        s.sendall(bytearray(MSG[:128], 'utf-8'))
        data = s.recv(152)
        print(str(data, 'utf-8'))
        s.close()

        #4 verdadeiro
