class Pong:

    def __init__(self, max_score):
        self.max_score = max_score
        self.score = [0, 0]
        self.player = 0

    def play(self, ball_pos, player_pos):
        if self.max_score in self.score:
            return 'Game Over!'
        if player_pos - 3 <= ball_pos <= player_pos + 3:
            self.player ^= 1
            return 'Player {} has hit the ball!'.format((self.player ^ 1) + 1)
        self.player ^= 1
        self.score[self.player] += 1
        if self.score[self.player] == self.max_score:
            return 'Player {} has won the game!'.format(self.player + 1)
        return 'Player {} has missed the ball!'.format((self.player ^ 1) + 1)
