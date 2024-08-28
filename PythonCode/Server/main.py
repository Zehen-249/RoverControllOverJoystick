from Server import  Server
from Arduino import Arduino


#initialize client-server connectivity
serverIP = "192.168.3.20"
port = 4444
server  = Server(serverIP,port)
server.connect()

#initialize arduino communication
ard_port = "COM3"
baud_rate = 9600
arduino = Arduino(ard_port,baud_rate)
arduino.connect()

while True:
    data = server.receive()
    if(not data):
        print("System Stopped!!")
        break
    # arduino.send(data)
server.close()

