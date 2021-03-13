import pygame
import sys
from random import randint
from settings import Settings
from board import Board
from start_menu import StartMenu
from scoreboard import Scoreboard


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
        self.scoreboard = Scoreboard(self)

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

    def check_win(self):
        """Check if someone has won the game, and draw a line if they have."""
        if self.board.squares_xo[1] == self.board.squares_xo[2] == self.board.squares_xo[3] != '':
            pygame.draw.line(self.screen, self.settings.win_line_color,
                             self.board.squares_coordinates[1], self.board.squares_coordinates[3], 10)
        elif self.board.squares_xo[4] == self.board.squares_xo[5] == self.board.squares_xo[6] != '':
            pygame.draw.line(self.screen, self.settings.win_line_color,
                             self.board.squares_coordinates[4], self.board.squares_coordinates[6], 10)
        elif self.board.squares_xo[7] == self.board.squares_xo[8] == self.board.squares_xo[9] != '':
            pygame.draw.line(self.screen, self.settings.win_line_color,
                             self.board.squares_coordinates[7], self.board.squares_coordinates[9], 10)
        elif self.board.squares_xo[1] == self.board.squares_xo[4] == self.board.squares_xo[7] != '':
            pygame.draw.line(self.screen, self.settings.win_line_color,
                             self.board.squares_coordinates[1], self.board.squares_coordinates[7], 10)
        elif self.board.squares_xo[2] == self.board.squares_xo[5] == self.board.squares_xo[8] != '':
            pygame.draw.line(self.screen, self.settings.win_line_color,
                             self.board.squares_coordinates[2], self.board.squares_coordinates[8], 10)
        elif self.board.squares_xo[3] == self.board.squares_xo[6] == self.board.squares_xo[9] != '':
            pygame.draw.line(self.screen, self.settings.win_line_color,
                             self.board.squares_coordinates[3], self.board.squares_coordinates[9], 10)
        elif self.board.squares_xo[1] == self.board.squares_xo[5] == self.board.squares_xo[9] != '':
            pygame.draw.line(self.screen, self.settings.win_line_color,
                             self.board.squares_coordinates[1], self.board.squares_coordinates[9], 10)
        elif self.board.squares_xo[3] == self.board.squares_xo[5] == self.board.squares_xo[7] != '':
            pygame.draw.line(self.screen, self.settings.win_line_color,
                             self.board.squares_coordinates[3], self.board.squares_coordinates[7], 10)

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        # Draw the start menu if the game is inactive,
        # else, draw the board, circles, and crosses.
        if not self.game_active:
            self.start_menu.draw_menu()
        else:
            self.screen.fill(self.settings.bg_color)
            self.board.draw_board()
            self.scoreboard.draw_scoreboard()

            for circle in self.board.circles:
                self.board.draw_circle(circle.image, circle.rect)
            for cross in self.board.crosses:
                self.board.draw_cross(cross.image, cross.rect)

            self.check_win()

        pygame.display.flip()


if __name__ == '__main__':
    ttt = TicTacToe()
    ttt.run_game()

# TODO: Make it possible for the player to change cross and circle colors, background colors, etc.