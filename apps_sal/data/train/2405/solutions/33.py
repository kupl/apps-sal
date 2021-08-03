class Solution:

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0

        for command in commands:
            if command == -2:
                di = (di - 1) % 4  # left
            elif command == -1:
                di = (di + 1) % 4  # right
            else:
                for _ in range(command):
                    if (x + dx[di], y + dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                    ans = max(ans, pow(x, 2) + pow(y, 2))

        return ans
