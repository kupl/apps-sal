class Pong:

    def __init__(self, max_score):
        self.max_score = max_score
        self.next = 1
        self.score = {1: 0, 2: 0}

    def play(self, ball, paddle):
        if max(self.score.values()) >= self.max_score:
            return 'Game Over!'
        (current, self.next) = (self.next, 3 - self.next)
        if paddle - 4 < ball < paddle + 4:
            msg = f'Player {current} has hit the ball!'
        else:
            msg = f'Player {current} has missed the ball!'
            self.score[current] += 1
            if self.score[current] == self.max_score:
                msg = f'Player {self.next} has won the game!'
        return msg
