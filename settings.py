import pygame.font


class Settings:
    """A class to store all settings for Tic Tac Toe."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen size settings).
        # Screen height should be a multiple of 3.
        self.screen_width = 1140
        self.screen_height = 840

        # Board settings.
        self.bg_color = (30, 30, 30)
        self.board_color = (255, 255, 255)
        self.win_line_color = (0, 255, 0)

        # Scoreboard settings.
        self.scoreboard_color = (200, 80, 200)
        self.scoreboard_text_color = (30, 30, 30)
        self.scoreboard_font = pygame.font.SysFont('Arial', 48)
