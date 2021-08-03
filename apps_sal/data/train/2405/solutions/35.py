class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0  # current position of robot
        dx, dy = 0, 1  # direction of robot
        obs = {tuple(i) for i in obstacles}  # create set of obstacles for faster access
        maxdist = 0  # store max distance after each command

        for step in commands:
            if 0 < step < 10:
                for i in range(step):
                    x, y = x + dx, y + dy  # take each step individually
                    if (x, y) in obs:  # take one step back if on an obstacle
                        x, y = x - dx, y - dy
                        break
            elif step == -2:  # change direction | move left
                dx, dy = -dy, dx
            elif step == -1:  # change direction | move right
                dx, dy = dy, -dx

            maxdist = max(maxdist, x**2 + y**2)

        return maxdist
