class Pong:
    def __init__(self, max_score):
        self.max_score = max_score;
        self.player=[0,0]
        self.index=0
        self.win=False
    def play(self, ball_pos, player_pos):
        if self.win:
            return "Game Over!"
        self.index+=1
        if abs(ball_pos-player_pos)>3:
            self.player[self.index%2]+=1
            if self.player[self.index%2]>=self.max_score:
                self.win=True
                return "Player 2 has won the game!" if self.index%2==1 else "Player 1 has won the game!"
            return "Player 1 has missed the ball!" if (self.index-1)%2==0 else "Player 2 has missed the ball!"
        return "Player 1 has hit the ball!" if (self.index-1)%2==0 else "Player 2 has hit the ball!"
