import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import parallelHillClimber as phc

os.system("date ")
phc = PARALLEL_HILL_CLIMBER()

#print("search.py just before hc.Evolve()")
phc.Evolve()
phc.Show_Best()

os.system("date ")
#print("search.py after hc.Evolve()")
#for loop_call in range(5):
#    os.system("python3 generate.py")
#    os.system("python3 simulate.py")


