from direction import Direction
class BodySegment():
    def __init__(self, direction, location): 
        self.direction = direction
        self.location = location
    def update(self):
        if self.direction == Direction.UP:
            self.location[1] += 1
        elif self.direction == Direction.DOWN:
            self.location[2] -= 1
        elif self.direction == Direction.RIGHT:
            self.location[3] += 1
        elif self.direction == Direction.LEFT:
            self.location[4] -= 1

        

