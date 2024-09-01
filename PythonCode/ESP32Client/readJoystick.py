import pygame 
import json

class Controller:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Initialize the joystick module
        pygame.joystick.init()

        # Initialize the joystick
        joysticks=pygame.joystick.get_count()
        if(joysticks>0):
            print("\nAvailable Controllers:")
            for i in range(joysticks):
                controller = pygame.joystick.Joystick(i)
                name = controller.get_name()
                print(f"Id {i}: {name}")
            
            self.instance_id = int(input(f"\nChoose the controller: "))

            if(self.instance_id<0 or self.instance_id>joysticks-1):
                print("No joystick with this ID ")
                pygame.quit()
                return None

            else:
                self._joystick = pygame.joystick.Joystick(self.instance_id)
                self.name = self._joystick.get_name()
                print(f"Joystick initialized: {self.name}\n")
        else:
            print("\nNo Controller Found\n")
            pygame.quit()
            return None
        
        self.data={}

    def get_axis_motion(self,event):
        max_speed = 200
        axis = event.axis
        value = round((event.value),2)
        if(axis == 1):
            if(value<-3.051e-5):
                data=f"Left speed {(abs(int(value*max_speed)))}"
                self.data["type"] = "LEFT"
                self.data["value"] = (abs(int(value*max_speed)))
            elif(value>0):
                data=f"right speed {value*max_speed}"
                self.data["type"] = "RIGHT"
                self.data["value"] = (abs(int(value*max_speed)))
            else:
                data=f"stop speed {0}"
                self.data["type"] = "STOP"
                self.data["value"] = 0
        elif(axis==2):
            if(value<-3.061e-05):
                data=f"Backward speed {(abs(int(value*max_speed)))}"
                self.data["type"] = "BACKWARD"
                self.data["value"] = (abs(int(value*max_speed)))
            elif(value>0):
                data=f"Forward speed {(abs(int(value*max_speed)))}"
                self.data["type"] = "FORWARD"
                self.data["value"] = (abs(int(value*max_speed)))
            else:
                data=f"stop speed {0}"
                self.data["type"] = "STOP"
                self.data["value"] = 0
        elif(axis==4):
            self.data["type"] = "axis 4"
            self.data["value"] = (abs(int(value*max_speed)))

        elif(axis==5):
            self.data["type"] = "axis 5"
            self.data["value"] = (abs(int(value*max_speed)))
        
        else:
            # print(f"Joystick {axis} value {value}")
            self.data['type']="STOP"
            self.data['value']=0

        return self.data
    
    def get_button_data(self,event):
        button = event.button
        if event.type == pygame.JOYBUTTONDOWN:
            self.data['type'] = f"Button {button}"
            self.data['value'] = "pressed"

        if event.type == pygame.JOYBUTTONUP:
            self.data['type'] = f"Button {button}"
            self.data['value'] = "released"

        return self.data
    
    def get_hat_data(self,event):
        data=None
        hat = event.button
        if event.type == pygame.JOYHATMOTION:
            hat = event.hat
            value = event.value
            data = f"Hat {hat} moved to {value}"
        return data
    