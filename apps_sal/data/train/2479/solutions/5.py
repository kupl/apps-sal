class Solution:

    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        (u, d, l, r) = map(moves.count, 'UDLR')
        return u == d and l == r
