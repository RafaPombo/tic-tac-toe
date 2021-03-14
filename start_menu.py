import pygame.font


class StartMenu:

    def __init__(self, ttt_game):
        """Initialize start menu attributes."""
        self.screen = ttt_game.screen
        self.screen_rect = self.screen.get_rect()

        self.menu_width = self.screen_rect.width
        self.menu_height = self.screen_rect.height
        self.menu_color = (0, 0, 255)
        self.menu_rect = pygame.Rect(0, 0, self.menu_width, self.menu_height)
        self.menu_rect.center = self.screen_rect.center

        self.button_width = self.menu_width * 2 / 3
        self.button_height = self.menu_height / 5
        self.button_color = (255, 255, 255)
        self.button_rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.button_rect.top = self.menu_rect.height / 10
        self.button_rect.centerx = self.menu_rect.centerx

        self.font = pygame.font.SysFont('Arial', 48)
        self.text_color = (0, 0, 0)
        self.button_msg = self.font.render('Play', True, self.text_color)
        self.msg_rect = self.button_msg.get_rect()
        self.msg_rect.center = self.button_rect.center

    def draw_menu(self):
        self.screen.fill(self.menu_color, self.menu_rect)
        self.screen.fill(self.button_color, self.button_rect)
        self.screen.blit(self.button_msg, self.msg_rect)
