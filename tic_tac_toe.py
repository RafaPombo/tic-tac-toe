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

        # If someone wins the game, store two values representing
        # the squares to draw a line on the board.
        self.game_over = []
        self.winner = ''

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
            if not self.game_over:
                self._check_square_click(mouse_pos)
            elif self.game_over:
                self.check_play_again_button(mouse_pos)
            self.check_restart_button(mouse_pos)
        else:
            play_button_clicked = self.start_menu.button_rect.collidepoint(mouse_pos)
            if play_button_clicked:
                self.game_active = True

    def check_play_again_button(self, mouse_pos):
        """Checks if the 'play again' button has been clicked."""
        button_clicked = self.scoreboard.play_again_rect.collidepoint(mouse_pos)
        if button_clicked:
            self.restart_game()

    def check_restart_button(self, mouse_pos):
        """Checks if the restart button has been clicked."""
        button_clicked = self.scoreboard.restart_text_rect.collidepoint(mouse_pos)
        if button_clicked:
            self.restart_game()

    def restart_game(self):
        """Restarts the game"""
        for circle in self.board.circles:
            self.board.circles.remove(circle)
        for cross in self.board.crosses:
            self.board.crosses.remove(cross)

        for square in self.board.squares:
            self.board.squares[square] = ''

        self.game_over = False

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
                self.check_win('Circle')
                if not self.game_over:
                    self._bot_turn()
                    self.check_win('Cross')
            elif square_tm_clicked and not self.board.squares[2]:
                self.board.create_circle(2)
                self.check_win('Circle')
                if not self.game_over:
                    self._bot_turn()
                    self.check_win('Cross')
            elif square_tr_clicked and not self.board.squares[3]:
                self.board.create_circle(3)
                self.check_win('Circle')
                if not self.game_over:
                    self._bot_turn()
                    self.check_win('Cross')
            elif square_ml_clicked and not self.board.squares[4]:
                self.board.create_circle(4)
                self.check_win('Circle')
                if not self.game_over:
                    self._bot_turn()
                    self.check_win('Cross')
            elif square_mm_clicked and not self.board.squares[5]:
                self.board.create_circle(5)
                self.check_win('Circle')
                if not self.game_over:
                    self._bot_turn()
                    self.check_win('Cross')
            elif square_mr_clicked and not self.board.squares[6]:
                self.board.create_circle(6)
                self.check_win('Circle')
                if not self.game_over:
                    self._bot_turn()
                    self.check_win('Cross')
            elif square_bl_clicked and not self.board.squares[7]:
                self.board.create_circle(7)
                self.check_win('Circle')
                if not self.game_over:
                    self._bot_turn()
                    self.check_win('Cross')
            elif square_bm_clicked and not self.board.squares[8]:
                self.board.create_circle(8)
                self.check_win('Circle')
                if not self.game_over:
                    self._bot_turn()
                    self.check_win('Cross')
            elif square_br_clicked and not self.board.squares[9]:
                self.board.create_circle(9)
                self.check_win('Circle')
                if not self.game_over:
                    self._bot_turn()
                    self.check_win('Cross')
        else:
            if square_tl_clicked and not self.board.squares[1]:
                self.board.create_cross(1)
                self.check_win('Cross')
                if not self.game_over:
                    self._bot_turn()
                    self.check_win('Circle')
            elif square_tm_clicked and not self.board.squares[2]:
                self.board.create_cross(2)
                self.check_win('Cross')
                if not self.game_over:
                    self._bot_turn()
                    self.check_win('Circle')
            elif square_tr_clicked and not self.board.squares[3]:
                self.board.create_cross(3)
                self.check_win('Cross')
                if not self.game_over:
                    self._bot_turn()
                    self.check_win('Circle')
            elif square_ml_clicked and not self.board.squares[4]:
                self.board.create_cross(4)
                self.check_win('Cross')
                if not self.game_over:
                    self._bot_turn()
                    self.check_win('Circle')
            elif square_mm_clicked and not self.board.squares[5]:
                self.board.create_cross(5)
                self.check_win('Cross')
                if not self.game_over:
                    self._bot_turn()
                    self.check_win('Circle')
            elif square_mr_clicked and not self.board.squares[6]:
                self.board.create_cross(6)
                self.check_win('Cross')
                if not self.game_over:
                    self._bot_turn()
                    self.check_win('Circle')
            elif square_bl_clicked and not self.board.squares[7]:
                self.board.create_cross(7)
                self.check_win('Cross')
                if not self.game_over:
                    self._bot_turn()
                    self.check_win('Circle')
            elif square_bm_clicked and not self.board.squares[8]:
                self.board.create_cross(8)
                self.check_win('Cross')
                if not self.game_over:
                    self._bot_turn()
                    self.check_win('Circle')
            elif square_br_clicked and not self.board.squares[9]:
                self.board.create_cross(9)
                self.check_win('Cross')
                if not self.game_over:
                    self._bot_turn()
                    self.check_win('Circle')

    def _bot_turn(self):
        """Place a cross or a circle in a random square."""

        # Code only gets executed if there are any squares left.
        if not self.game_over:

            # Select a random square.
            square = randint(1, 9)

            # If the square selected is already filled, select another square.
            while self.board.squares[square]:
                square = randint(1, 9)

            if self.circle_turn:
                self.board.create_circle(square)
            else:
                self.board.create_cross(square)

    def check_win(self, winner):
        """Check if someone has won the game, and draw a line if they have."""
        if self.board.squares[1] == self.board.squares[2] == self.board.squares[3] != '':
            self.game_over = [1, 3]
            self.winner = winner
        elif self.board.squares[4] == self.board.squares[5] == self.board.squares[6] != '':
            self.game_over = [4, 6]
            self.winner = winner
        elif self.board.squares[7] == self.board.squares[8] == self.board.squares[9] != '':
            self.game_over = [7, 9]
            self.winner = winner
        elif self.board.squares[1] == self.board.squares[4] == self.board.squares[7] != '':
            self.game_over = [1, 7]
            self.winner = winner
        elif self.board.squares[2] == self.board.squares[5] == self.board.squares[8] != '':
            self.game_over = [2, 8]
            self.winner = winner
        elif self.board.squares[3] == self.board.squares[6] == self.board.squares[9] != '':
            self.game_over = [3, 9]
            self.winner = winner
        elif self.board.squares[1] == self.board.squares[5] == self.board.squares[9] != '':
            self.game_over = [1, 9]
            self.winner = winner
        elif self.board.squares[3] == self.board.squares[5] == self.board.squares[7] != '':
            self.game_over = [3, 7]
            self.winner = winner

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

            if self.game_over:
                self.board.draw_win_line(self.game_over)
                self.scoreboard.show_game_over(self.winner)
        pygame.display.flip()


if __name__ == '__main__':
    ttt = TicTacToe()
    ttt.run_game()

# TODO: Make it possible for the player to change cross and circle colors, background colors, etc.
