class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        for move in moves:
            # print(move)
            if move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
            elif move == 'U':
                x += 1
            elif move == 'D':
                x -= 1

        if x == 0 and y == 0:
            return True
        else:
            return False
