import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.indexRange)

    def Get_Value(self,i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)  
