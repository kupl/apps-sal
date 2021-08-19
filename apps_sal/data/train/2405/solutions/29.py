class Solution:

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = y = d = ans = 0
        obs = set(map(tuple, obstacles))
        move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in commands:
            if i == -2:
                d = (d - 1) % 4
            elif i == -1:
                d = (d + 1) % 4
            else:
                for j in range(i):
                    if (x + move[d][0], y + move[d][1]) not in obs:
                        x += move[d][0]
                        y += move[d][1]
                        ans = max(ans, x ** 2 + y ** 2)
        return ans
