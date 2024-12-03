# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
import sys

from constants import *
from player import Player, Shot
from shot import  Shot
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in updatable:
            thing.update(dt)

        for obj in asteroids:
            if obj.collide(player):
                print("Game over!")
                sys.exit()

            for s in shots:
                if obj.collide(s):
                    obj.split()
                    s.kill()

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        delta = clock.tick(60)
        dt = delta / 1000


if __name__ == "__main__":
    main()
