from Client import Client
from readJoystick import Controller 
import pygame 

# Initialize pygame and joystick
controller = Controller()


try:
    if(controller.name):
        # Set up the display
        screen = pygame.display.set_mode((640, 480))  # Width x Height

        #Initialize client-server connectivity
        ESPIP = "192.168.19.144"
        port = 12345
        client = Client(ESPIP,port)
        client.connect()

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
                print(data)
                client.send(data)
except Exception as e :
    print(e)

