class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = (0, 1)
        start = [0, 0]
        obstacleSet = set(map(tuple, obstacles))
        ans = 0
        for cmd in commands:
            if cmd == -2:
                direction = (-direction[1], direction[0])
            elif cmd == -1:
                direction = (direction[1], -direction[0])
            else:
                for g in range(cmd):
                    if (start[0] + direction[0], start[1] + direction[1]) not in obstacleSet:
                        start[1] += direction[1]
                        start[0] += direction[0]
                        ans = max(ans, start[0]**2 + start[1]**2)
        return ans
