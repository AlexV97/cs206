import math

import pybullet

import pyrosim.pyrosim as pyrosim

import pyrosim.constants as c

class NEURON: 

    def __init__(self,line):
 
        #print("neuron constructor - c.MOTOR_NEURON=", c.MOTOR_NEURON) #c.MOTOR_NEURON= = 1
        #print("")

        self.Determine_Name(line)

        self.Determine_Type(line)

        self.Search_For_Link_Name(line)

        self.Search_For_Joint_Name(line)

        self.Set_Value(0.0)

    def Add_To_Value( self, value ):

        self.Set_Value( self.Get_Value() + value )

    def Get_Joint_Name(self):

        return self.jointName

    def Get_Link_Name(self):

        return self.linkName

    def Get_Name(self):

        return self.name

    def Get_Value(self):

        return self.value

    def Is_Sensor_Neuron(self):

        return self.type == c.SENSOR_NEURON

    def Is_Hidden_Neuron(self):

        return self.type == c.HIDDEN_NEURON

    def Is_Motor_Neuron(self):
        print("neuron - Is_Motor_Neuron(self) - type=", self.type, " - value=", self.value)
        return self.type == c.MOTOR_NEURON

    def Print(self):
        #print("neuron Print - name:")
        #self.Print_Name()
        #print("neuron Print - type:")
        #self.Print_Type()
        print("neuron Print - value:")
        self.Print_Value()

        print("")

    def Set_Value(self,value):

        self.value = value

    def Update_Sensor_Neuron(self):
        pyrosim.Get_Touch_Sensor_Value_For_Link(self.Get_Link_Name())
        
    def Update_Hidden_Or_Motor_Neuron(self):
        self.Set_Value(0.0)
        #self.value = 0
# -------------------------- Private methods -------------------------

    def Determine_Name(self,line):

        if "name" in line:

            splitLine = line.split('"')

            self.name = splitLine[1]

    def Determine_Type(self,line):

        if "sensor" in line:

            self.type = c.SENSOR_NEURON

        elif "motor" in line:

            self.type = c.MOTOR_NEURON

        else:

            self.type = c.HIDDEN_NEURON

    def Print_Name(self):

       print(self.name)

    def Print_Type(self):

       print(self.type)

    def Print_Value(self):

       print(self.value , " " , end="" )

    def Search_For_Joint_Name(self,line):

        if "jointName" in line:

            splitLine = line.split('"')

            self.jointName = splitLine[5]

    def Search_For_Link_Name(self,line):

        if "linkName" in line:

            splitLine = line.split('"')

            self.linkName = splitLine[5]

    def Threshold(self):

        self.value = math.tanh(self.value)
