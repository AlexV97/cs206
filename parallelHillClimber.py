import copy
import constants as c
import csv
import os
import time
import numpy
from array import *
from solution import SOLUTION
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf    2>nul ")
        os.system("rm fitness*.nndf  2>nul ")
        self.parents = {}
        self.nextAvailableID = 0
        self.Best_Fitness_array = []

        for entry_key in range(0,c.populationSize):
            self.parents[entry_key] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
    
    def Evolve(self):
        #print("parallelHillClimber - Evolve()")
        self.Evaluate(self.parents)
        for gen in range( c.numberOfGenerations):
            self.currentGeneration = gen
            self.Evolve_For_One_Generation()
            self.Save_BestFitnessInGenToArray()
        self.Write_BestFitnessArrayToFile()
          
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Select()
        #self.Print() # while debugging


    def Spawn(self):
        self.children = {}
        for i, parent in self.parents.items():
            self.children[i] = copy.deepcopy(parent)
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        
    def Mutate(self):
        for i, child in self.children.items():
            child.Mutate()

    def Select(self):
        for entry_key in range(0,c.populationSize):
            if ( self.children[entry_key].fitness < self.parents[entry_key].fitness ):
                self.parents[entry_key] = self.children[entry_key]
        
#    def Print(self):
#        #print("parallelHillClimber - Print()")
#        print("")
#        for entry_key in range(0,c.populationSize):
#            print("phc Print() entry_key= " , entry_key, " - Parent Fitness= ", self.parents[entry_key].fitness, " - Child Fitness= ", #self.children[entry_key].fitness)
#        print("")

    def Show_Best(self):
        #print("parallelHillClimber - Show_Best() c.populationSize= ", c.populationSize)
        entry_key_lowest_parent = -1

        lowest_fitness=999
        for entry_key in range(0,c.populationSize):
            #print("parallelHillClimber - Show_Best() entry_key= ", entry_key, " - self.parents[entry_key].fitness= ", self.parents[entry_key].fitness)
            if ( self.parents[entry_key].fitness < lowest_fitness ):
                entry_key_lowest_parent = entry_key
                lowest_fitness          = self.parents[entry_key].fitness
            
        print("parallelHillClimber - Show_Best() key= ", entry_key_lowest_parent, " - Lowest fitness= ", lowest_fitness)
        self.parents[entry_key_lowest_parent].Start_Simulation("GUI", 1)
                
    
    def Evaluate(self, solutions):
        #print("parallelHillClimber - Evaluate()")
        for entry_key in range(0,c.populationSize):
            solutions[entry_key].Start_Simulation("DIRECT", 0)
        #print("parallelHillClimber - Evaluate() - All Simulation Started")
        for entry_key in range(0,c.populationSize):
            solutions[entry_key].Wait_For_Simulation_To_End("DIRECT")
        #print("parallelHillClimber - Evaluate() - All Simulation Completed")
            
    def Save_BestFitnessInGenToArray(self):
        entry_key_lowest_parent = -1
        
        lowest_fitness=999
        for entry_key in range(0,c.populationSize):
            if ( self.parents[entry_key].fitness < lowest_fitness ):
                entry_key_lowest_parent = entry_key
                lowest_fitness          = self.parents[entry_key].fitness
                
        self.Best_Fitness_array.append(lowest_fitness)
            
        print("parallelHillClimber - Save_BestFitnessInGenToArray() key= ", entry_key_lowest_parent, " - Lowest fitness= ", lowest_fitness)

            
    def Write_BestFitnessArrayToFile(self):
#### saving .txt
        fitnessFileName = "../data_hexapod/Cumulative_BestFitness_PerGeneration.txt"

        f_write = open(fitnessFileName, "w+")

        new_array = numpy.array(self.Best_Fitness_array)
        s_new_array = str(new_array)
        f_write.write(s_new_array)
        f_write.close()
###        fitnessFileName = "../data_hexapod/Cumulative_BestFitness_PerGeneration.csv"
###        new_array = numpy.array(self.Best_Fitness_array)
###        s_new_array = str(new_array)
###
###        with open(fitnessFileName, 'w', newline='') as f_write:
###            fitnessToWrite = csv.writer(f_write, delimiter=',')
###            fitnessToWrite.writerows(s_new_array)
            
        print("parallelHillClimber - Write_BestFitnessArrayToFile() ")
