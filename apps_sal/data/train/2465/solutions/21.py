class Solution:
    def divisorGame(self, N: int) -> bool:
        turns = [{2:1}, {2:0}]
        
        def play(turn, N):
            if N in turns[turn]:
                return turns[turn][N]
            
            if turn:
                win = all(play(0, N-x) for x in range(1, N) if N % x == 0)
            else:
                win = any(play(1, N-x) for x in range(1, N) if N % x == 0)
            
            return turns[turn].setdefault(N, win)
        
        return play(0, N)
