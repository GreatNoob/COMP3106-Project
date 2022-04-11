from re import T
import pygame

import settings
from Game.Controllers.game import Game


def main():
    pygame.init()
    pygame.font.init()
    window = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
    pygame.display.set_caption('Chess')
    icon = pygame.transform.smoothscale(pygame.image.load(settings.ICON_PATH), (settings.ICON_SIZE, settings.ICON_SIZE))
    pygame.display.set_icon(icon)
    
    game = Game(window)
    game.start(True)
    pygame.quit()


if __name__ == "__main__":
    main()


