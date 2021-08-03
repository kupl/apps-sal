from itertools import cycle


class Pong:
    def __init__(self, max_score):
        self.max_score = max_score
        self.scores = {1: 0, 2: 0}
        self.players = cycle((1, 2))

    def game_over(self):
        return any(score >= self.max_score for score in list(self.scores.values()))

    def play(self, ball_pos, player_pos):
        if self.game_over():
            return "Game Over!"

        player = next(self.players)
        if abs(ball_pos - player_pos) <= 3:
            return "Player {} has hit the ball!".format(player)
        else:
            self.scores[player] += 1
            if self.scores[player] == self.max_score:
                return "Player {} has won the game!".format(next(self.players))
            else:
                return "Player {} has missed the ball!".format(player)
