class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

       # moves = list(moves)
       # u = moves.count('U')
       # d = moves.count('D')
       # l = moves.count('L')
       # r = moves.count('R')
       # if u == d and l == r:
       #     return True
       # else:
       #     return False
       # return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
        u, d, l, r = map(moves.count, 'UDLR')
        return u == d and l == r
