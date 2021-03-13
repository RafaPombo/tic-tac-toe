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

        # Create a group to store circles and crosses.
        self.circles = pygame.sprite.Group()
        self.crosses = pygame.sprite.Group()

        # Create a rect for each of the 4 board lines.
        self.r1_rect = pygame.Rect(0, self.screen.get_height() / 3, self.screen.get_height(), 10)
        self.r2_rect = pygame.Rect(0, 2 * self.screen.get_height() / 3, self.screen.get_height(), 10)
        self.c1_rect = pygame.Rect(self.r1_rect.width / 3, 0, 10, self.screen.get_height())
        self.c2_rect = pygame.Rect(2 * self.r1_rect.width / 3, 0, 10, self.screen.get_height())

        # Get the coordinates for the center of each row and column.
        self.coordinates = {
            1: self.screen.get_height() / 6,
            2: self.screen.get_height() / 2,
            3: self.screen.get_height() * 5 / 6
        }

        # Get the coordinates for the center of each square
        #            COLUMN                 ROW
        self.squares_coordinates = {
            1: (self.coordinates[1], self.coordinates[1]),
            2: (self.coordinates[2], self.coordinates[1]),
            3: (self.coordinates[3], self.coordinates[1]),
            4: (self.coordinates[1], self.coordinates[2]),
            5: (self.coordinates[2], self.coordinates[2]),
            6: (self.coordinates[3], self.coordinates[2]),
            7: (self.coordinates[1], self.coordinates[3]),
            8: (self.coordinates[2], self.coordinates[3]),
            9: (self.coordinates[3], self.coordinates[3]),
        }

        """Create a rect for each square in the board and position it correctly."""
        # The sides of each square should be equal to one third the sides of the rows and columns,
        # with a subtracted 9 pixels to compensate for the board itself.
        self.square_width = self.square_height = int((self.c1_rect.height / 3) - 9)

        self.square_tl = pygame.Rect(0, 0, self.square_width, self.square_height)
        self.square_tl.bottom = self.r1_rect.top
        self.square_tl.right = self.c1_rect.left

        self.square_tm = pygame.Rect(0, 0, self.square_width, self.square_height)
        self.square_tm.bottom = self.r1_rect.top
        self.square_tm.left = self.c1_rect.right

        self.square_tr = pygame.Rect(0, 0, self.square_width, self.square_height)
        self.square_tr.bottom = self.r1_rect.top
        self.square_tr.left = self.c2_rect.right

        self.square_ml = pygame.Rect(0, 0, self.square_width, self.square_height)
        self.square_ml.top = self.r1_rect.bottom
        self.square_ml.right = self.c1_rect.left

        self.square_mm = pygame.Rect(0, 0, self.square_width, self.square_height)
        self.square_mm.top = self.r1_rect.bottom
        self.square_mm.left = self.c1_rect.right

        self.square_mr = pygame.Rect(0, 0, self.square_width, self.square_height)
        self.square_mr.top = self.r1_rect.bottom
        self.square_mr.left = self.c2_rect.right

        self.square_bl = pygame.Rect(0, 0, self.square_width, self.square_height)
        self.square_bl.top = self.r2_rect.bottom
        self.square_bl.right = self.c1_rect.left

        self.square_bm = pygame.Rect(0, 0, self.square_width, self.square_height)
        self.square_bm.top = self.r2_rect.bottom
        self.square_bm.left = self.c1_rect.right

        self.square_br = pygame.Rect(0, 0, self.square_width, self.square_height)
        self.square_br.top = self.r2_rect.bottom
        self.square_br.left = self.c2_rect.right

        # Keep track of occupied squares.
        self.squares = {
            1: False, 2: False, 3: False,
            4: False, 5: False, 6: False,
            7: False, 8: False, 9: False,
        }

        # Keep track of which squares have crosses or circles on them.
        self.squares_xo = {
            1: '', 2: '', 3: '',
            4: '', 5: '', 6: '',
            7: '', 8: '', 9: ''
        }

    def draw_board(self):
        """Draw the board lines."""
        for rect in [self.r1_rect, self.r2_rect, self.c1_rect, self.c2_rect]:
            pygame.draw.rect(self.screen, self.board_color, rect, border_radius=5)

    def create_circle(self, square):
        """Create a circle object."""
        new_circle = Circle(self)
        new_circle.rect.center = self.squares_coordinates[square]
        self.circles.add(new_circle)

        self.squares[square] = True
        self.squares_xo[square] = 'circle'

        self.ttt_game.circle_turn = False
        self.ttt_game.cross_turn = True

    def draw_circle(self, surface, rect):
        """Draw a circle object."""
        self.screen.blit(surface, rect)

    def create_cross(self, square):
        """Create a cross object."""
        new_cross = Cross(self)
        new_cross.rect.center = self.squares_coordinates[square]
        self.crosses.add(new_cross)

        self.squares[square] = True
        self.squares_xo[square] = 'cross'

        self.ttt_game.cross_turn = False
        self.ttt_game.circle_turn = True

    def draw_cross(self, surface, rect):
        """Draw a cross object."""
        self.screen.blit(surface, rect)


class Circle(Sprite):

    def __init__(self, board):
        super().__init__()
        self.board = board

        self.image = pygame.image.load('images/circle.png')
        self.scale_size = (int(self.board.square_width * 3 / 4), int(self.board.square_height * 3 / 4))
        self.image = pygame.transform.scale(self.image, (self.scale_size))

        self.rect = self.image.get_rect()


class Cross(Sprite):

    def __init__(self, board):
        super().__init__()
        self.board = board

        self.image = pygame.image.load('images/cross.png')
        self.scale_size = (int(self.board.square_width * 3 / 4), int(self.board.square_height * 3 / 4))
        self.image = pygame.transform.scale(self.image, (self.scale_size))

        self.rect = self.image.get_rect()
