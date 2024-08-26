import serial
import time

class Arduino:
    def __init__(self,arduino_port:str,baud_rate:int):
        self.arduino_port = arduino_port  # Replace with the appropriate port name
        self.baud_rate = baud_rate  # Set the baud rate for the Arduino communication
    
    def connect(self):
        try:
            self._arduino = serial.Serial(self.arduino_port, self.baud_rate)
            time.sleep(2)
        except Exception as e:
            print(f"Could not Connect\n{e}")

    def send(self,data):
        self._arduino.write(data.encode('utf-8'))