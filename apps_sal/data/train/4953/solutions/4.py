class Pong:
    def __init__(self, max_score):
        self.max_score = max_score
        self.scores = [0, 0]
        self.turn = 0

    def play(self, ball_pos, player_pos):
        try:
            if max(self.scores) == self.max_score:
                return 'Game Over!'
            if abs(ball_pos - player_pos) <= 3:
                return f'Player {self.turn + 1} has hit the ball!'
            self.scores[1 - self.turn] += 1
            if self.scores[1 - self.turn] == self.max_score:
                return f'Player {2 - self.turn} has won the game!'
            else:
                return f'Player {self.turn + 1} has missed the ball!'    
        finally:
            self.turn = (self.turn + 1) % 2
