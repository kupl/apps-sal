class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        x = y = 0
        max_dist = 0
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        obstacles = set(tuple(x) for x in obstacles)
        direction = 0

        for command in commands:

            if command == -1:

                direction += 1

                if direction == 4:
                    direction = 0

            elif command == -2:

                direction -= 1

                if direction == -1:
                    direction = 3

            else:

                new_x, new_y = directions[direction]

                while command > 0 and (x + new_x, y + new_y) not in obstacles:

                    x += new_x
                    y += new_y
                    command -= 1

                max_dist = max(max_dist, x**2 + y**2)

        return max_dist
