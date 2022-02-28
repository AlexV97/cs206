import numpy
import constants as c
import pybullet as p
import math
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = numpy.zeros(c.indexRange)

        self.Prepare_To_Act()
        
    #def Prepare_To_Act(self, amplitude, frequency, offset):
    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.offset    = c.phaseOffset
        #self.frequency = c.frequency
        if (self.jointName == "Torso_BackLeg"):
            self.frequency = c.frequency/2
        else:
            self.frequency = c.frequency

        print("MOTOR Prepare_To_Act jointName=", self.jointName, " - frequency=", self.frequency)

        for i in range(c.indexRange):
            self.motorValues[i] = numpy.sin(math.pi/4)*numpy.sin(((i*2*self.frequency*math.pi/(c.indexRange))+self.offset))

    #def Set_Value(self,i, currentrobot):
    def Set_Value(self,desiredAngle, currentrobot):
        #self.motorValues[i] = numpy.sin(math.pi/4)*numpy.sin(((i*2*self.frequency*math.pi/(c.indexRange))+self.offset))
#        self.motorValues[i] = pyrosim.Set_Motor_For_Joint(
        desiredAngle = pyrosim.Set_Motor_For_Joint(
            bodyIndex = currentrobot.robotId,  #robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            #targetPosition = self.amplitude * self.motorValues[i],
            targetPosition = self.amplitude * desiredAngle,
            maxForce = 80)

