from readJoystick import Controller
from Client import Client
import json
import pygame 

#initialize controller
controller = Controller()

try:
    if(controller.name):
        # Set up the display
        screen = pygame.display.set_mode((640, 480))  # Width x Height

        #Initialize client-server connectivity
        # serverIp = "192.168.3.20"
        # port = 4444
        # client=Client(serverIp,port)
        # client.connect()

        # Read Joystick
        running = True 
        while running:
            data=None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.JOYAXISMOTION:
                    data = controller.get_axis_motion(event)
                    
                if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP:
                    data = controller.get_button_data(event)

                if event.type ==  pygame.JOYHATMOTION:
                    data = controller.get_hat_data(event)
                
            if(data):
                print(json.dumps(data))
                # client.send(json.dumps(data))
except Exception as e :
    pass

