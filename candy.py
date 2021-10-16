import random

class Candy():

    def __init__(self, location):
        self.location = location
        self.eaten = False
    
    def getLocation(self):
        return self.location

    def destroy(self):
        self.eaten = True
