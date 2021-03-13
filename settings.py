class Settings:
    """A class to store all settings for Tic Tac Toe."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen size settings (screen is a square).
        self.screen_width = self.screen_height = 850

        # Color settings.
        self.bg_color = (30, 30, 30)
        self.board_color = (255, 255, 255)
        self.cross_color = (0, 0, 255)
        self.circle_color = (255, 0, 0)
        self.win_line_color = (0, 255, 0)
