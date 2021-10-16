from direction import Direction


class Player():

    def __init__(self, direction, head):
        self.head = BodySegment(direction, head)
        self.body = [head]

        
        
    def turnLeft(self):
        if self.head.getDirection() is not Direction.RIGHT:
            self.head.getDirection() = Direction(self.head.getDirection().value -1)

    def turnRight(self):
        if self.head.getDirection() is not Direction.LEFT:
            self.head.getDirection() = Direction(self.head.getDirection().value +1)
    
    def getBody(self):
        return self.body

    def getHeadLocation (self):
        return self.head.getLocation()
    
    def eat (self):
        self.grow()

    def grow(self):
        lastBodySeg = self.body[-1]
        self.body.append(BodySegment(lastBodySeg.getDirection(), lastBodySeg.getPrevLocation()))
    
    def update(self):
        self.BodySegment.update


