class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        def isint(num):
            try:
                int(num)
                return True
            except ValueError:
                return False
        score_board = []
        for i in ops:
            if isint(i):
                score_board.append(int(i))
            elif i == 'C':
                score_board.pop()
            elif i == 'D':
                score_board.append(score_board[-1] * 2)
            elif i == '+':
                score_board.append(sum(score_board[-2:]))
        return sum(score_board)
