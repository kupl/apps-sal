class Solution:

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        obs = set(map(tuple, obstacles))
        (x, y, direction, result) = (0, 0, 0, 0)
        for cmd in commands:
            if cmd == -1:
                direction = (direction + 1) % 4
            elif cmd == -2:
                direction = (direction - 1) % 4
            else:
                for _ in range(cmd):
                    (nx, ny) = (x + dx[direction], y + dy[direction])
                    if (nx, ny) in obs:
                        break
                    (x, y) = (nx, ny)
            result = max(result, x ** 2 + y ** 2)
        return result
