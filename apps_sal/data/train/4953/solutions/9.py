class Pong:

    def __init__(self, max_score):
        self.max_score = max_score
        self.i = -1
        self.event = 'Player {} has {} the ball!'
        self.score = {1: 0, 2: 0}

    def play(self, ball, player):
        if self.event:
            self.i += 1
        if not self.event:
            return 'Game Over!'
        hit = abs(player - ball)
        if hit > 3:
            winer = (1, 2)[not self.i % 2]
            self.score[winer] += 1
            if self.score[winer] == self.max_score:
                self.event = None
                return f'Player {winer} has won the game!'
        return self.event.format((1, 2)[self.i % 2], ('hit', 'missed')[hit > 3])
