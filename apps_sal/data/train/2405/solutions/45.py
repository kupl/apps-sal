class Solution:

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = y = 0
        dx = 0
        dy = 1
        ans = 0
        o_dict = {}
        for obstacle in obstacles:
            o_dict[tuple(obstacle)] = True
        for command in commands:
            if command == -2:
                (dx, dy) = (-dy, dx)
            elif command == -1:
                (dy, dx) = (-dx, dy)
            else:
                for k in range(command):
                    if (x + dx, y + dy) not in o_dict.keys():
                        x += dx
                        y += dy
                        ans = max(ans, x ** 2 + y ** 2)
                    else:
                        break
        return ans
