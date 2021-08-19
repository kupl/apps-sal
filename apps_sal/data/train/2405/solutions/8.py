class Solution:

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        x = 0
        y = 0
        obs = set([tuple(x) for x in obstacles])
        res = 0
        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d - 1 + 4) % 4
            else:
                (dx, dy) = dirs[d]
                for i in range(c):
                    if (x + dx, y + dy) not in obs:
                        x += dx
                        y += dy
                        res = max(res, x * x + y * y)
        return res
