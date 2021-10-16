from direction import Direction


class Player():
    # initilizes head and body
    def __init__(self, direction, head):
        self.head = BodySegment(direction, head)
        self.body = [head]


    # function that turns head's direction to left 
    def turnLeft(self):
        if self.head.getDirection() is not Direction.RIGHT:
            self.head.setNextDirection(Direction(self.head.getDirection().value -1))
    
    # function that turns head's direction to left
    def turnRight(self):
        if self.head.getDirection() is not Direction.LEFT:
            self.head.setNextDirection(Direction(self.head.getDirection().value +1))
    # gets body
    def getBody(self):
        return self.body

    # gets head's location
    def getHeadLocation (self):
        return self.head.getLocation()
    
    #calls grow on itself to eat
    def eat (self):
        self.grow()

    # increases body size
    def grow(self):
        lastBodySeg = self.body[-1]
        self.body.append(BodySegment(lastBodySeg.getDirection(), lastBodySeg.getPrevLocation()))
    
    # updates body
    def update(self, width):
        for segment in self.body:
            segment.update(width)
        for i in range(1, len(self.body)):
            self.body[i].setNextDirection(self.body[i-1].getDirection())
        
    #checks to see if snake collides   
    def collided(self):
        return self.selfCollision() or self.wallCollision()

    #checks to see if snake collides with itself
    def selfCollision(self):
        return self.getHeadLocation() in [self.body[i].getLocation() for i in range(1, len(self.body))]

    #checks to see if snake collides with wall
    def wallCollision(self):
        return self.getHeadLocation() > 7 or self.getHeadLocation() < 0

    #returns head's previous location
    def getPrevLocation(self):
        return self.head.getPrevLocation()
        
    #creturns head location
    def getLocation(self):
        return self.head.getLocation()
