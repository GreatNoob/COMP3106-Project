from unittest import TestCase
import pygame
import settings
from Game.Controllers.game import Game

class TestGame(TestCase):

    def setUp(self):
        pygame.init()
        pygame.font.init()
        self.window = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        pygame.display.set_caption('Chess')
        icon = pygame.transform.smoothscale(pygame.image.load(settings.ICON_PATH), (settings.ICON_SIZE, settings.ICON_SIZE))
        pygame.display.set_icon(icon)

    def test_self_play(self):
        game = Game(self.window)
        game.start()
        pygame.quit()

    def test_against_ai(self):
        game = Game(self.window)
        game.start(start_ai=True)
        pygame.quit()

    def test_ai_self_play(self):
        game = Game(self.window)
        game.start(start_ai=True, self_play=True)
        pygame.quit()