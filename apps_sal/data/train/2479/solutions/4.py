class Solution:
    def judgeCircle(self, moves):
        l, r, u, d = list(map(moves.count, 'LRUD'))
        return l == r and u == d
