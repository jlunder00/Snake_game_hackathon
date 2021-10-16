from candy import Candy
from player import Player
from direction import Direction
from body_segment import BodySegment
import random
import opc, time
client = opc.Client('localhost:7890')

class World():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.numLEDs = width*height
        self.pixels = [(0,0,0)]*self.numLEDs
        self.board = [[0 for j in range(self.width)] for i in range(self.height)]
        head = (random.randint(0, self.width-1), random.randint(0, self.height-1))
        direction = random.choice(list(Direction))
        self.player = Player(direction, head)
        self.cur_candy = self.spawn_candy(self.player.getBody())
        self.game_over = False

    def getPlayer(self):
        return self.player

    def spawn_candy(self, playerBody):
        location = (random.randint(0, self.width-1), random.randint(0, self.height-1))
        while location in [segment.getLocation() for segment in playerBody]:
            location = (random.randint(0, self.width-1), random.randint(0, self.height-1))
        self.pixels[location[0]+((self.width)*location[1])] = (0, 255, 0)
        return Candy(location)

    def update(self):
        self.player.update(self, self.width)
        if not self.player.collided():
            for segment in self.player.getBody():
                prevLocation = segment.getPrevLocation()
                location = segment.getLocation()
                self.pixels[(prevLocation[1]*(self.width))+prevLocation[0]] = (0, 0, 0)
                self.pixels[(location[1]*(self.width))+location[0]] = (255, 0, 0)
            client.put_pixels(self.pixels)
            if self.player.getHeadLocation() == self.cur_candy.getLocation():
                self.player.eat()
                self.cur_candy.destroy()
                self.cur_candy = self.spawn_candy(self.player.getBody())
        
        if self.player.collided():
            self.game_over = True
        





