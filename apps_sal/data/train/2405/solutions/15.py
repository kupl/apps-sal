class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        if not commands:
            return 0

        x, y, res = 0, 0, 0

        directions = {0: 1, 1: 1, 2: -1, 3: -1}
        cur_dir = 1

        obs = set(map(tuple, obstacles))

        for cmd in commands:
            if cmd == -2:
                cur_dir = (cur_dir + 1) % 4
            elif cmd == -1:
                cur_dir = (cur_dir + 3) % 4
            else:
                t = directions[cur_dir]
                x_move, y_move = (t, 0) if cur_dir in (0, 2) else (0, t)
                for _ in range(cmd):
                    if (x + x_move, y + y_move) not in obs:
                        x += x_move
                        y += y_move
                        res = max(res, (x**2 + y**2))
                    else:
                        break
        return res
