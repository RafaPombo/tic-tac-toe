import pygame
import sys
from random import randint
from settings import Settings
from board import Board
from start_menu import StartMenu


class TicTacToe:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Tic Tac Toe')

        self.start_menu = StartMenu(self)
        self.board = Board(self)

        self.circle_turn = False
        self.cross_turn = True

        self.game_active = False

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
        if self.game_active:
            self._check_square_click(mouse_pos)
        else:
            play_button_clicked = self.start_menu.button_rect.collidepoint(mouse_pos)
            if play_button_clicked:
                self.game_active = True

    def _check_square_click(self, mouse_pos):
        """Checks which square was clicked."""
        square_tl_clicked = self.board.square_tl.collidepoint(mouse_pos)
        square_tm_clicked = self.board.square_tm.collidepoint(mouse_pos)
        square_tr_clicked = self.board.square_tr.collidepoint(mouse_pos)
        square_ml_clicked = self.board.square_ml.collidepoint(mouse_pos)
        square_mm_clicked = self.board.square_mm.collidepoint(mouse_pos)
        square_mr_clicked = self.board.square_mr.collidepoint(mouse_pos)
        square_bl_clicked = self.board.square_bl.collidepoint(mouse_pos)
        square_bm_clicked = self.board.square_bm.collidepoint(mouse_pos)
        square_br_clicked = self.board.square_br.collidepoint(mouse_pos)

        if self.circle_turn:
            if square_tl_clicked and not self.board.squares[1]:
                self.board.create_circle(1)
                self._bot_turn()
            elif square_tm_clicked and not self.board.squares[2]:
                self.board.create_circle(2)
                self._bot_turn()
            elif square_tr_clicked and not self.board.squares[3]:
                self.board.create_circle(3)
                self._bot_turn()
            elif square_ml_clicked and not self.board.squares[4]:
                self.board.create_circle(4)
                self._bot_turn()
            elif square_mm_clicked and not self.board.squares[5]:
                self.board.create_circle(5)
                self._bot_turn()
            elif square_mr_clicked and not self.board.squares[6]:
                self.board.create_circle(6)
                self._bot_turn()
            elif square_bl_clicked and not self.board.squares[7]:
                self.board.create_circle(7)
                self._bot_turn()
            elif square_bm_clicked and not self.board.squares[8]:
                self.board.create_circle(8)
                self._bot_turn()
            elif square_br_clicked and not self.board.squares[9]:
                self.board.create_circle(9)
                self._bot_turn()
        else:
            if square_tl_clicked and not self.board.squares[1]:
                self.board.create_cross(1)
                self._bot_turn()
            elif square_tm_clicked and not self.board.squares[2]:
                self.board.create_cross(2)
                self._bot_turn()
            elif square_tr_clicked and not self.board.squares[3]:
                self.board.create_cross(3)
                self._bot_turn()
            elif square_ml_clicked and not self.board.squares[4]:
                self.board.create_cross(4)
                self._bot_turn()
            elif square_mm_clicked and not self.board.squares[5]:
                self.board.create_cross(5)
                self._bot_turn()
            elif square_mr_clicked and not self.board.squares[6]:
                self.board.create_cross(6)
                self._bot_turn()
            elif square_bl_clicked and not self.board.squares[7]:
                self.board.create_cross(7)
                self._bot_turn()
            elif square_bm_clicked and not self.board.squares[8]:
                self.board.create_cross(8)
                self._bot_turn()
            elif square_br_clicked and not self.board.squares[9]:
                self.board.create_cross(9)
                self._bot_turn()

    def _bot_turn(self):
        """Place a cross or a circle in a random square."""

        # Code only gets executed if there are any squares left.
        if not all(self.board.squares[square] is True for square in self.board.squares):

            # Select a random square.
            square = randint(1, 9)

            # If the square selected is already filled, select another square.
            while self.board.squares[square]:
                square = randint(1, 9)

            if self.circle_turn:
                self.board.create_circle(square)
            else:
                self.board.create_cross(square)

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.board.draw_board()

        for circle in self.board.circles:
            self.board.draw_circle(circle.surface, circle.circle_rect)
        for cross in self.board.crosses:
            self.board.draw_cross(cross.surface, cross.cross_rect)

        if not self.game_active:
            self.start_menu.draw_menu()

        pygame.display.flip()


if __name__ == '__main__':
    ttt = TicTacToe()
    ttt.run_game()
