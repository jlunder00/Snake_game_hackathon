import pygame
from world import World
from player import Player
from direction import Direction

def main():
    pygame.init()
    window = pygame.display.set_mode((300,300))
    clock = pygame.time.Clock()
    world = World(8, 8)
    while world.game_over != True:
        clock.tick(1)
        player = world.getPlayer()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                d = player.getDirection()
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if d == Direction.UP:
                        player.turnRight()
                    elif d == Direction.DOWN:
                        player.turnLeft()
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if d == Direction.DOWN:
                        player.turnRight()
                    elif d == Direction.UP:
                        player.turnLeft()
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    if d == Direction.RIGHT:
                        player.turnLeft()
                    elif d == Direction.LEFT:
                        player.turnRight()
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if d == Direction.LEFT:
                        player.turnLeft()
                    elif d == Direction.RIGHT:
                        player.turnRight()
        world.update()

if __name__ == "__main__":
    main()
