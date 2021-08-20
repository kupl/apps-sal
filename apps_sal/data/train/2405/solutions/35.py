class Solution:

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        (x, y) = (0, 0)
        (dx, dy) = (0, 1)
        obs = {tuple(i) for i in obstacles}
        maxdist = 0
        for step in commands:
            if 0 < step < 10:
                for i in range(step):
                    (x, y) = (x + dx, y + dy)
                    if (x, y) in obs:
                        (x, y) = (x - dx, y - dy)
                        break
            elif step == -2:
                (dx, dy) = (-dy, dx)
            elif step == -1:
                (dx, dy) = (dy, -dx)
            maxdist = max(maxdist, x ** 2 + y ** 2)
        return maxdist
