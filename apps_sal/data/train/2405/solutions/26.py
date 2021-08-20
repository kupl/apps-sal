class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 0
    curr_coords = (0, 0)

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        max_distance = 0
        obstacles = set((tuple(obstacle) for obstacle in obstacles))
        for command in commands:
            if command == -2:
                self.dir_idx = (self.dir_idx - 1) % 4
            if command == -1:
                self.dir_idx = (self.dir_idx + 1) % 4
            else:
                for i in range(command):
                    (x_move, y_move) = self.directions[self.dir_idx]
                    new_coords_x = self.curr_coords[0] + x_move
                    new_coords_y = self.curr_coords[1] + y_move
                    if (new_coords_x, new_coords_y) in obstacles:
                        break
                    self.curr_coords = (new_coords_x, new_coords_y)
                    max_distance = max(max_distance, sum((coord ** 2 for coord in self.curr_coords)))
        return max_distance
