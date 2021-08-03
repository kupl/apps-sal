PADDLE_SIZE = 7


class Pong:
    def __init__(self, max_score):
        self.max_score = max_score

        self.player_scores = {0: 0, 1: 0}

        self.current_player = 0
        self.game_state = None

    def play(self, ball_pos, player_pos):

        if self.game_state is not None:
            return self.game_state

        paddle_range = (player_pos - (PADDLE_SIZE / 2),
                        player_pos + (PADDLE_SIZE / 2))

        if ball_pos > max(paddle_range) or ball_pos < min(paddle_range):

            self.player_scores[self.current_player ^ 1] += 1

            if self.player_scores[self.current_player ^ 1] >= self.max_score:
                self.game_state = "Game Over!"
                string = "Player {} has won the game!".format(self.current_player ^ 1 + 1)
            else:
                string = "Player {} has missed the ball!".format(self.current_player + 1)

        else:
            string = "Player {} has hit the ball!".format(self.current_player + 1)

        self.switch_player()
        return string

    def switch_player(self):
        self.current_player ^= 1
