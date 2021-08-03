class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        curr = [0, 0]
        ori = 0
        obstacles = {tuple(obs) for obs in obstacles}
        maxx = 0
        for cmd in commands:
            if cmd == -2:
                ori = (ori - 1) % 4
            elif cmd == -1:
                ori = (ori + 1) % 4
            else:
                for _ in range(cmd):
                    nexxt = [curr[0] + directions[ori][0], curr[1] + directions[ori][1]]
                    if tuple(nexxt) not in obstacles:
                        curr = nexxt
                        maxx = max(maxx, curr[0]**2 + curr[1]**2)
        return maxx
