import pygame
from world import World
from player import Player

def main():
    world = World(8, 8)
    while world.game_over != True:
        world.update()
