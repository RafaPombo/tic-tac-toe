import pygame.font


class Scoreboard:

    def __init__(self, ttt_game):
        """Initialize scorekeeping attributes."""
        self.ttt_game = ttt_game
        self.screen = ttt_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ttt_game.settings

        self.player_score = 0
        self.opponent_score = 0

        scoreboard_width = self.screen_rect.width - self.ttt_game.board.r1_rect.width
        scoreboard_height = self.screen_rect.height
        self.scoreboard_rect = pygame.Rect(0, 0, scoreboard_width, scoreboard_height)
        self.scoreboard_rect.bottomright = self.screen_rect.bottomright

        self.button_width = self.scoreboard_rect.width * 4 / 5
        self.button_height = self.screen_rect.height / 10

        self.restart_text = self.settings.scoreboard_font.render('RESTART', True, self.settings.scoreboard_text_color,
                                                                 self.settings.button_color)
        self.restart_text_rect = self.restart_text.get_rect()
        self.restart_text_rect.center = self.scoreboard_rect.center

        self.opponent_text = self.settings.scoreboard_font.render('OPPONENT', True, self.settings.scoreboard_text_color)
        self.opponent_text_rect = self.opponent_text.get_rect()
        self.opponent_text_rect.centerx = self.scoreboard_rect.centerx
        self.opponent_text_rect.bottom = self.scoreboard_rect.bottom - 10

        self.opponent_score_text = self.settings.scoreboard_font.render(str(self.opponent_score), True,
                                                                        self.settings.scoreboard_text_color)
        self.opponent_score_text_rect = self.opponent_score_text.get_rect()
        self.opponent_score_text_rect.centerx = self.scoreboard_rect.centerx
        self.opponent_score_text_rect.bottom = self.opponent_text_rect.top - 5

        self.dashes = self.settings.scoreboard_font.render('-----------', True, self.settings.scoreboard_text_color)
        self.dashes_rect = self.dashes.get_rect()
        self.dashes_rect.centerx = self.scoreboard_rect.centerx
        self.dashes_rect.bottom = self.opponent_score_text_rect.top - 5

        self.player_score_text = self.settings.scoreboard_font.render(str(self.player_score), True,
                                                                      self.settings.scoreboard_text_color)
        self.player_score_text_rect = self.player_score_text.get_rect()
        self.player_score_text_rect.centerx = self.scoreboard_rect.centerx
        self.player_score_text_rect.bottom = self.dashes_rect.top - 5

        self.player_text = self.settings.scoreboard_font.render('PLAYER', True, self.settings.scoreboard_text_color)
        self.player_text_rect = self.player_text.get_rect()
        self.player_text_rect.centerx = self.scoreboard_rect.centerx
        self.player_text_rect.bottom = self.player_score_text_rect.top - 5

    def draw_scoreboard(self):
        pygame.draw.rect(self.screen, self.settings.scoreboard_color, self.scoreboard_rect)
        self.screen.blit(self.restart_text, self.restart_text_rect)

        # Draw the score on the scoreboard
        self.screen.blit(self.opponent_text, self.opponent_text_rect)
        self.screen.blit(self.opponent_score_text, self.opponent_score_text_rect)
        self.screen.blit(self.dashes, self.dashes_rect)
        self.screen.blit(self.player_score_text, self.player_score_text_rect)
        self.screen.blit(self.player_text, self.player_text_rect)

    def show_game_over(self, xo):
        xo_text = self.settings.scoreboard_font.render(xo, True, self.settings.scoreboard_text_color)
        xo_rect = xo_text.get_rect()
        xo_rect.centerx = self.scoreboard_rect.centerx
        xo_rect.y = 10

        wins_text = self.settings.scoreboard_font.render('wins!', True, self.settings.scoreboard_text_color)
        wins_rect = wins_text.get_rect()
        wins_rect.centerx = self.scoreboard_rect.centerx
        wins_rect.top = xo_rect.bottom + 5

        play_again_text = self.settings.scoreboard_font.render('PLAY AGAIN', True, self.settings.scoreboard_text_color,
                                                               self.settings.button_color)
        self.play_again_rect = play_again_text.get_rect()
        self.play_again_rect.centerx = self.scoreboard_rect.centerx
        self.play_again_rect.top = wins_rect.bottom + 5

        self.screen.blit(xo_text, xo_rect)
        self.screen.blit(wins_text, wins_rect)
        self.screen.blit(play_again_text, self.play_again_rect)
