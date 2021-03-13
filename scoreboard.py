import pygame.font


class Scoreboard:

    def __init__(self, ttt_game):
        """Initialize scorekeeping attributes."""
        self.ttt_game = ttt_game
        self.screen = ttt_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ttt_game.settings
