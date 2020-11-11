import random
import math
import numpy as np
from pprint import pprint
from flappybird import FlappyBird

class Agent:
    def __init__(self):
        self.flappybird =  FlappyBird();
       

    def init(self):    
        pass

    """
     * Method used to determine the next move to be performed by the agent.
     * now is moving random
     """

    def act(self): 
        self.observeworld()
        if self.myRandom() == 2:
            self.flappybird.holdKeyDown()        
        else:
            self.flappybird.releaseKey()

    def myRandom(self):
        return random.randint(0, 10)

    def observeworld(self):
        positions = self.flappybird.getWorldPositionObjets()
        print("Upper block: ", positions[0])
        print("Bottom block: ", positions[1])
        print("Bird: ", positions[2])
        print("Count: ",self.flappybird.counter)
        print("Dead: ", self.flappybird.dead)



    def run(self):  
        self.flappybird.initGame()
        while True:
            self.flappybird.eachCicle()            
            self.act()

