from direction import Direction
class BodySegment():
    def __init__(self, direction, location): 
        self.direction = direction
        self.nextDirection = direction
        self.location = location
        self.prevLocation = location
    def update(self, rowWidth):
        self.direction = self.nextDirection
        self.prevLocation = self.location
        if self.direction == Direction.UP:
            self.location[1] = (self.location[0], self.location[1]-rowWidth)
        elif self.direction == Direction.DOWN:
            self.location[1] = = (self.location[0], self.location[1]+rowWidth)
        elif self.direction == Direction.RIGHT:
            self.location = (self.location[0]+1, self.location[1])
        elif self.direction == Direction.LEFT:
            self.location[0] = (self.location[0]-1, self.location[1])
    def getLocation(self):
        return self.location

    def getPrevLocation(self):
        return self.prevLocation

    def setNextDirection(self, direction):
        self.nextDirection = direction

    def getDirection(self):
        return self.direction

   

        

