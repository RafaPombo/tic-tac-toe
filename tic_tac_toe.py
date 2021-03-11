import pygame
import sys
from settings import Settings
from board import Board


class TicTacToe:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Tic Tac Toe')

        self.board = Board(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to game events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_mousedown_events(mouse_pos)

    def _check_mousedown_events(self, mouse_pos):
        """Respond to mouse presses."""
        square_tl_clicked = self.board.square_tl.collidepoint(mouse_pos)
        square_tm_clicked = self.board.square_tm.collidepoint(mouse_pos)
        square_tr_clicked = self.board.square_tr.collidepoint(mouse_pos)
        square_ml_clicked = self.board.square_ml.collidepoint(mouse_pos)
        square_mm_clicked = self.board.square_mm.collidepoint(mouse_pos)
        square_mr_clicked = self.board.square_mr.collidepoint(mouse_pos)
        square_bl_clicked = self.board.square_bl.collidepoint(mouse_pos)
        square_bm_clicked = self.board.square_bm.collidepoint(mouse_pos)
        square_br_clicked = self.board.square_br.collidepoint(mouse_pos)

        if square_tl_clicked and not self.board.squares[1]:
            self.board.create_cross(1)
            self.board.squares[1] = True
        elif square_tm_clicked and not self.board.squares[2]:
            self.board.create_circle(2)
            self.board.squares[2] = True
        elif square_tr_clicked and not self.board.squares[3]:
            self.board.create_circle(3)
            self.board.squares[3] = True
        elif square_ml_clicked and not self.board.squares[4]:
            self.board.create_circle(4)
            self.board.squares[4] = True
        elif square_mm_clicked and not self.board.squares[5]:
            self.board.create_circle(5)
            self.board.squares[5] = True
        elif square_mr_clicked and not self.board.squares[6]:
            self.board.create_circle(6)
            self.board.squares[6] = True
        elif square_bl_clicked and not self.board.squares[7]:
            self.board.create_circle(7)
            self.board.squares[7] = True
        elif square_bm_clicked and not self.board.squares[8]:
            self.board.create_circle(8)
            self.board.squares[8] = True
        elif square_br_clicked and not self.board.squares[9]:
            self.board.create_cross(9)
            self.board.squares[9] = True

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.board.prep_board()

        for circle in self.board.circles:
            self.board.draw_circle(circle.surface, circle.circle_rect)
        for cross in self.board.crosses:
            self.board.draw_cross(cross.surface, cross.cross_rect)

        pygame.display.flip()


if __name__ == '__main__':
    ttt = TicTacToe()
    ttt.run_game()
