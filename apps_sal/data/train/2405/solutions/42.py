class Solution:

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = {tuple(i) for i in obstacles}
        (x, y) = (0, 0)
        (dx, dy) = (0, 1)
        maxdist = 0
        for i in commands:
            if 1 <= i <= 9:
                for j in range(i):
                    (x, y) = (x + dx, y + dy)
                    if (x, y) in obs:
                        (x, y) = (x - dx, y - dy)
                        break
            elif i == -2:
                (dx, dy) = (-dy, dx)
            elif i == -1:
                (dx, dy) = (dy, -dx)
            maxdist = max(maxdist, x ** 2 + y ** 2)
        return maxdist
