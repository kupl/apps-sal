class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        # LC solution copy
        '''
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        x = y = di = 0

        obstacleSet = set(map(tuple,obstacles))
        ans = 0

        for cmd in commands:
            if cmd == -2: # left
                di = (di - 1) % 4
            elif cmd == -1: # right
                di = (di + 1) % 4
            else:
                for k in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)

        return ans
        '''

        # My attempt failed with incorrect answer for some large input, so above is LC copy, Fixed the mistake in code below,
        # Basically we are asked for maximum distance the robot went, not the distance to final destination.

        # -2: turn left 90 degrees
        # -1: turn right 90 deg
        # 1 <= x <= 9 forward x units

        # obstacle[i][0], obstacles[i][1] is an obstacle

        # Calculate euclidean distance from origin.

        # check obstacle at every move and apply the distance and turns he can perform.

        # cmd[i]
        # position[i] = position[i-1] + min(cmd[i], blocked())

        obstacleSet = set()

        for p in obstacles:
            obstacleSet.add(tuple(p))

        dirs = [1, 1, -1, -1]  # must be 1 for west and north, -1 for east and south

        axis = [0, 1]  # must be 0 for east and west, 1 for north and south.

        position = [0, 0]

        ax = 1  # Along Y axis
        up = 0  # Facing north
        result = 0
        for cmd in commands:

            if cmd > 0:
                # scan for obstacle and limit move up to the obstacle
                nextstop = list(position)
                for c in range(cmd):

                    nextstop[ax] = nextstop[ax] + (dirs[up])

                    if tuple(nextstop) in obstacleSet:
                        break
                    position = list(nextstop)
                    result = max(result, position[0]**2 + position[1]**2)

            elif cmd == -2:
                ax = (ax + 1) % 2
                up = (up + 3) % 4  # Left
            elif cmd == -1:
                ax = (ax + 1) % 2
                up = (up + 1) % 4  # Right

            # print(prev, \"->\", position, ax, up)

        return result
