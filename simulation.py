from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR 

import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

class SIMULATION:
    def __init__(self, directOrGUI):
        self.directOrGUI = directOrGUI
        #print("simulation - constructor")
        if ( self.directOrGUI == "DIRECT" ):
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
            
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
        
    def Run(self):
        print("simulation - Run()")
        for i in range(c.indexRange):
           #print("simulation - i=", i)
           #print("simulation - p.stepSimulation()")
           p.stepSimulation()
           #print("simulation - self.robot.Sense(i)")
           self.robot.Sense(i)
           #print("simulation - self.robot.Think()")
           self.robot.Think()
           #print("simulation - self.robot.Act()")
           self.robot.Act(i)
           if ( self.directOrGUI == "GUI"):
                time.sleep(1/960); #time.sleep(1/480);
        
        self.robot.Save_Values_Sensors()
    
    def Get_Fitness(self):
        print("simulation Get_Fitness() Starts")
        self.robot.Get_Fitness()
        print("simulation Get_Fitness() Done")
            
    def __del__(self):
        p.disconnect()

