'''
Amy Green - 200930437
5990M: Introduction to Programming for Geopgraphical Information Analysis - Core Skills
Assignment 1: Building a Simple Agent Based Model (ABM)
_version 1.0_

The agent framework holds a basic Agent class to allow movement within a 2D plane environment which incorporates interaction between all other agents within this shared environment. 
'''

import random
class Agent(object):
    #Provides a class for multiple agents that move and interact within an environment. 
    
    def __init__(self, environment, agents, i, y = None, x = None): 
        #Assigning variables - __init function assigns values to classes
        
        if (x == None):
            self._x = random.randint(0,299)
        else:
            self._x = x
        
        if (y == None):
            self._y = random.randint(0,299)
        else:
            self._y = y 
        '''Adjusted function header to ensure same starting point every time model is run, was initially the code below:'''
        #self._x = random.randint(0,99) - Assigning random variables to x value
        #self._y = random.randint(0,99) - Assigning random variables to y value
        
        self.environment = environment #Creating an environment for all agents to interact
        self.agents = agents #Reference for all individual agents within the environment
        self.store = 0 #Allocating a store per agents to harvest environment values
        self.i = i #Place ID on agent to be able to test stores have increased
        
    def __str__(self):
        return "i" + str(self.i) + " x " + str(self._x) + ", y " + str(self._y)
        #Returns agent description with location and store amount 
        
#Moves agents randomly within the 2D environment.        
    def move(self):
        if random.random() <0.5:
            self._y = (self._y + 1) % 300
        else: 
            self._y = (self._y - 1) % 300

        if random.random() <0.5:
            self._x = (self._x + 1) % 300
        else:
            self._x = (self._x - 1) % 300
            
#Gets agents by defining each with a property.           
    def getx(self):
        return self._x
    
    def gety(self):
        return self._y
    
#Make agents eat part of the environment and store the value.
    def eat(self): 
        if self.environment[self._y][self._x]>10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
            
#Share stores with neighbouring agents.
            #Neighbourhood = the distance within which agents share 
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            if agent != self: #Don't share with self
                 dist = self.distance_between(agent) 
                 if dist <= neighbourhood:
                     sum = self.store + agent.store
                     ave = sum /2
                     self.store = ave
                     agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))
    
#Work out and return distance between self and neighbour.
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5 
        
        
        
    

            