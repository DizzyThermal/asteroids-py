from constants import *
from player import Player

import pygame


FPS = 60


def main():
    # Create Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create Game Clock
    clock = pygame.time.Clock()

    # Create Player (Triangle)
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)

    # Game Loop
    dt = 0
    while True:
        # If Close [X] is clicked, quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the Screen (Black)
        screen.fill((0, 0, 0))

        # Draw Player
        player.update(dt)
        player.draw(screen)


        # Update Display
        pygame.display.flip()

        # Tick clock (FPS) and store clock delta
        dt = clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()

