import sys
import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
        
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    asterioid_field = AsteroidField()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for sprite in updatable:
            sprite.update(dt)
        
        for sprite in asteroids:
            if sprite.is_colliding(player):
                print("Game Over!")
                sys.exit()

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = game_clock.tick(60) / 1000



if __name__ == "__main__":
    main()

