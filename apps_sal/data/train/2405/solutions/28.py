class Solution:

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
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
        """
        obstacleSet = set()
        for p in obstacles:
            obstacleSet.add(tuple(p))
        dirs = [1, 1, -1, -1]
        axis = [0, 1]
        position = [0, 0]
        ax = 1
        up = 0
        result = 0
        for cmd in commands:
            if cmd > 0:
                nextstop = list(position)
                for c in range(cmd):
                    nextstop[ax] = nextstop[ax] + dirs[up]
                    if tuple(nextstop) in obstacleSet:
                        break
                    position = list(nextstop)
                    result = max(result, position[0] ** 2 + position[1] ** 2)
            elif cmd == -2:
                ax = (ax + 1) % 2
                up = (up + 3) % 4
            elif cmd == -1:
                ax = (ax + 1) % 2
                up = (up + 1) % 4
        return result
