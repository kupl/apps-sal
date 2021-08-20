class Solution:

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        o_set = set(map(tuple, obstacles))
        res = 0
        for cmd in commands:
            if cmd == -2:
                di = (di - 1) % 4
            elif cmd == -1:
                di = (di + 1) % 4
            else:
                for _ in range(cmd):
                    if (x + dx[di], y + dy[di]) not in o_set:
                        x += dx[di]
                        y += dy[di]
                        res = max(res, x * x + y * y)
        return res
