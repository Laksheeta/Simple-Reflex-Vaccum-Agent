import random

class Environment(object):
    def __init__(self):
        self.locationCondition = {'A': '0', 'B': '0'}
        self.locationCondition['A'] = random.randint(0, 1)
        self.locationCondition['B'] = random.randint(0, 1)

class SimpleReflexVacuumAgent(Environment):
    def __init__(self, Environment):
        print (Environment.locationCondition)
        Score = 0
        vacuumLocation = random.randint(0, 1)
        if vacuumLocation == 0:
            print ("Vacuum is randomly placed at Location A.")
            print ("Location A is Dirty.") if Environment.locationCondition['A'] == 1 else print("Location A is Clean.")
            if Environment.locationCondition['A'] == 1:
                Environment.locationCondition['A'] = 0
                Score += 1
                print ("Location A has been Cleaned.") 
            print ("Moving to Location B...")
            print ("Location B is Dirty.") if Environment.locationCondition['B'] == 1 else print("Location B is Clean.")
            if Environment.locationCondition['B'] == 1:
                Environment.locationCondition['B'] = 0;
                Score += 1
                print ("Location B has been Cleaned.")
            print("Environment is Clean.")
                
        elif vacuumLocation == 1:
            print ("Vacuum randomly placed at Location B.")
            print ("Location B is Dirty.") if Environment.locationCondition['B'] == 1 else print("Location B is Clean.")
            if Environment.locationCondition['B'] == 1:
                Environment.locationCondition['B'] = 0
                Score += 1
                print ("Location B has been Cleaned.")
            print ("Moving to Location A...")
            print ("Location A is Dirty.") if Environment.locationCondition['A'] == 1 else print("Location A is Clean.")
            if Environment.locationCondition['A'] == 1:
                Environment.locationCondition['A'] = 0;
                Score += 1
                print ("Location A has been Cleaned.")
            print("Environment is Clean.")    
            
        print (Environment.locationCondition)
        print ("Performance Measurement: " + str(Score))

theEnvironment = Environment()
theVacuum = SimpleReflexVacuumAgent(theEnvironment)