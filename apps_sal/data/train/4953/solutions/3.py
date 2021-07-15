class Pong:
    def __init__(self, win):
        self.win = win
        self.turn = -1
        self.scores = [0, 0]

    def play(self, ball, player):
        
        if max(self.scores) == self.win: return 'Game Over!'
            
        self.turn = (self.turn + 1) % 2
        
        if abs(ball - player) < 4: return 'Player ' + str(self.turn + 1) + ' has hit the ball!'

        self.scores[(self.turn + 1) % 2] += 1
            
        return 'Player ' + (str(1 if self.turn else 2) + ' has won the game!' if max(self.scores) == self.win else str(self.turn + 1) + ' has missed the ball!')
