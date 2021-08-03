class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d_id = 0

        obs = set()
        for o in obstacles:
            obs.add(tuple(o))

        x = 0
        y = 0
        best = 0
        for i in range(len(commands)):
            if commands[i] == -1:
                d_id = (d_id + 1) % 4
            elif commands[i] == -2:
                d_id = (d_id - 1) % 4
            else:
                while commands[i] > 0:
                    if (x + directions[d_id][0], y + directions[d_id][1]) not in obs:
                        x += directions[d_id][0]
                        y += directions[d_id][1]
                        best = max(best, x**2 + y**2)
                    else:
                        break
                    commands[i] -= 1

        return best
