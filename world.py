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
        head = (random.randint(0, self.width), random.randint(0, self.height))
        direction = random.choice(list(Direction))
        self.player = Player(direction, head)
        self.cur_candy = self.spawn_candy(self.player.getBody())
        self.game_over = False

    def spawn_candy(self, playerBody):
        location = (random.randint(0, self.width), random.randint(0, self.height))
        while segment.getLocation() in playerBody:
            location =(random.randint(0, self.width), random.randint(0, self.height))
        return Candy(location)

    def update(self):
        self.player.update()
        if self.player.getHeadLocation() == self.cur_candy.getLocation():
            self.player.eat()
            self.cur_candy.destroy()
            self.cur_candy = self.spawn_candy(self.player.getBody())
        
        if self.player.collided():
            self.game_over = True
        





