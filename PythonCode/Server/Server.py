import socket

class Server:
    def __init__(self,serverIp:str,port:int):
        self.serverIp = serverIp
        self.port = port
        self._conn = None
        self._addr = None

    def connect(self):
        print("Server IP Address: ",self.serverIp,"\nPORT: ",self.port)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind((self.serverIp, self.port))
            sock.listen(1)
            self._conn, self._addr = sock.accept()

            print('Connected by', self._addr)
        except Exception as e:
            print(f"Could Not connect\n{e}")

    def receive(self):
        data = self._conn.recv(1024).decode()
        return data
    def  close(self):
        self._conn.close()
