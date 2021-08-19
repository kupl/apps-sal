class Solution:

    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        pos = [0, 0]
        for i in moves:
            if i == 'U':
                pos[0] = pos[0] + 1
            elif i == 'D':
                pos[0] = pos[0] - 1
            elif i == 'L':
                pos[1] = pos[1] - 1
            elif i == 'R':
                pos[1] = pos[1] + 1
        return [0, 0] == pos
