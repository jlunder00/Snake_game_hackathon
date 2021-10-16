from candy import Candy
from player import Player
from direction import Direction
from body_segment import BodySegment
import random

class World():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0 for j in range(self.width)] for i in range(self.height)]
        head = random.randint(0, 7)
        direction = random.choice(list(Direction))
        self.player = Player(direction, head)
        self.cur_candy = self.spawn_candy(self.player.getBody())

    def spawn_candy(self, playerBody):
        location = (random.randint(0, 7), random.randint(0, 7))
        while segment.getLocation() in playerBody:
            location = (random.randint(0, 7), random.randint(0, 7))
        return Candy(location)




