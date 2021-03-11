import pygame
from settings import Settings
from pygame.sprite import Sprite


class Board:
    """A class to store the board."""

    def __init__(self, ttt_game):
        """Initialize board attributes."""
        self.ttt_game = ttt_game
        self.settings = Settings()
        self.screen = ttt_game.screen
        self.screen_rect = self.screen.get_rect()
        self.board_color = self.settings.board_color

        self.circles = pygame.sprite.Group()
        self.crosses = pygame.sprite.Group()

        # Keep track of occupied squares.
        self.squares = {
            1: False, 2: False, 3: False,
            4: False, 5: False, 6: False,
            7: False, 8: False, 9: False,
        }

    def prep_board(self):
        """Draw the board."""
        # Draw each of the 4 board lines.
        r1_rect = pygame.Rect(0, self.screen.get_height() / 3, self.screen.get_height(), 10)
        r2_rect = pygame.Rect(0, 2 * self.screen.get_height() / 3, self.screen.get_height(), 10)
        c1_rect = pygame.Rect(self.screen.get_width() / 3, 0, 10, self.screen.get_height())
        c2_rect = pygame.Rect(2 * self.screen.get_width() / 3, 0, 10, self.screen.get_height())

        r1_rect.centerx = self.screen.get_rect().centerx
        r2_rect.centerx = self.screen.get_rect().centerx
        c1_rect.centerx = r1_rect.x + r1_rect.width / 3
        c2_rect.centerx = r1_rect.x + 2 * r1_rect.width / 3

        pygame.draw.rect(self.screen, self.board_color, r1_rect, border_radius=3)
        pygame.draw.rect(self.screen, self.board_color, r2_rect, border_radius=3)
        pygame.draw.rect(self.screen, self.board_color, c1_rect, border_radius=3)
        pygame.draw.rect(self.screen, self.board_color, c2_rect, border_radius=3)

        # Get the coordinates for the center of each square.
        self.rows = {
            1: self.screen.get_height() / 6,
            2: self.screen.get_height() / 2,
            3: 5 * self.screen.get_height() / 6
        }

        self.columns = {
            1: r1_rect.x + r1_rect.width / 6,
            2: r1_rect.x + r1_rect.width / 2,
            3: r1_rect.x + 5 * r1_rect.width / 6
        }

        self.squares_coordinates = {
            1: (self.columns[1], self.rows[1]), 2: (self.columns[2], self.rows[1]), 3: (self.columns[3], self.rows[1]),
            4: (self.columns[1], self.rows[2]), 5: (self.columns[2], self.rows[2]), 6: (self.columns[3], self.rows[2]),
            7: (self.columns[1], self.rows[3]), 8: (self.columns[2], self.rows[3]), 9: (self.columns[3], self.rows[3]),
        }

        width = height = c1_rect.height / 3 - 9

        self.square_tl = pygame.Rect(0, 0, width, height)
        self.square_tl.bottom = r1_rect.top
        self.square_tl.right = c1_rect.left

        self.square_tm = pygame.Rect(0, 0, width, height)
        self.square_tm.bottom = r1_rect.top
        self.square_tm.left = c1_rect.right

        self.square_tr = pygame.Rect(0, 0, width, height)
        self.square_tr.bottom = r1_rect.top
        self.square_tr.left = c2_rect.right

        self.square_ml = pygame.Rect(0, 0, width, height)
        self.square_ml.top = r1_rect.bottom
        self.square_ml.right = c1_rect.left

        self.square_mm = pygame.Rect(0, 0, width, height)
        self.square_mm.top = r1_rect.bottom
        self.square_mm.left = c1_rect.right

        self.square_mr = pygame.Rect(0, 0, width, height)
        self.square_mr.top = r1_rect.bottom
        self.square_mr.left = c2_rect.right

        self.square_bl = pygame.Rect(0, 0, width, height)
        self.square_bl.top = r2_rect.bottom
        self.square_bl.right = c1_rect.left

        self.square_bm = pygame.Rect(0, 0, width, height)
        self.square_bm.top = r2_rect.bottom
        self.square_bm.left = c1_rect.right

        self.square_br = pygame.Rect(0, 0, width, height)
        self.square_br.top = r2_rect.bottom
        self.square_br.left = c2_rect.right

    def create_circle(self, square):
        new_circle = Circle()
        new_circle.circle_rect.center = self.squares_coordinates[square]
        self.circles.add(new_circle)

    def draw_circle(self, surface, rect):
        self.screen.blit(surface, rect)

    def create_cross(self, square):
        new_cross = Cross()
        new_cross.cross_rect.center = self.squares_coordinates[square]

        self.crosses.add(new_cross)

    def draw_cross(self, surface, rect):
        self.screen.blit(surface, rect)


class Circle(Sprite):

    def __init__(self):
        super().__init__()
        self.settings = Settings()

        pygame.font.init()
        self.myfont = pygame.font.SysFont('Arial', 300)

        self.surface = self.myfont.render('o', True, self.settings.circle_color)
        self.circle_rect = self.surface.get_rect()


class Cross(Sprite):

    def __init__(self):
        super().__init__()
        self.settings = Settings()

        pygame.font.init()
        self.myfont = pygame.font.SysFont('Arial', 300)

        self.surface = self.myfont.render('x', True, self.settings.cross_color)
        self.cross_rect = self.surface.get_rect()
