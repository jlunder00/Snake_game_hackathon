

class World():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0 for j in range(self.width)] for i in range(self.height)]
        
