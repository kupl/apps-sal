class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        obstacles = set([tuple(x) for x in obstacles])

        face = 0  # NESW = 0123
        x, y = 0, 0
        max_dist = 0
        for command in commands:
            if command == -2:
                face = (face - 1) % 4
            elif command == -1:
                face = (face + 1) % 4
            else:
                if face == 0:
                    for i in range(1, command + 1):
                        if (x, y + i) in obstacles:
                            i -= 1
                            break
                    y += i

                elif face == 1:
                    for i in range(1, command + 1):
                        if (x + i, y) in obstacles:
                            i -= 1
                            break
                    x += i

                elif face == 2:
                    for i in range(1, command + 1):
                        if (x, y - i) in obstacles:
                            i -= 1
                            break
                    y -= i

                else:
                    for i in range(1, command + 1):
                        if (x - i, y) in obstacles:
                            i -= 1
                            break
                    x -= i

                max_dist = max(max_dist, x**2 + y**2)

        return max_dist
