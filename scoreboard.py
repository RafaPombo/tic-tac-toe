import pygame.font


class Scoreboard:

    def __init__(self, ttt_game):
        """Initialize scorekeeping attributes."""
        self.ttt_game = ttt_game
        self.screen = ttt_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ttt_game.settings

        scoreboard_width = self.screen_rect.width - self.ttt_game.board.r1_rect.width
        scoreboard_height = self.screen_rect.height
        self.scoreboard_rect = pygame.Rect(0, 0, scoreboard_width, scoreboard_height)
        self.scoreboard_rect.bottomright = self.screen_rect.bottomright

    def draw_scoreboard(self):
        pygame.draw.rect(self.screen, self.settings.scoreboard_color, self.scoreboard_rect)