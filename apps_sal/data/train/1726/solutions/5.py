def path_finder(maze):
    maze_object = Maze(maze)
    if maze_object.maze[maze_object.exit[0]][maze_object.exit[1]] == 'W':
        return False
    return maze_object.recursive_path((0, 0))


class Maze:
    previous_positions = []
    exit = None
    dimension_maze = None
    maze = None

    def __init__(self, maze):
        self.maze = self.transform(maze)
        self.exit = (len(self.maze) - 1, len(self.maze[0]) - 1)
        self.dimension_maze = (self.exit[0], self.exit[1])
        self.previous_positions = []

    def transform(self, maze):
        return [row for row in maze.split('\n')]

    def recursive_path(self, current_position):
        if current_position == self.exit:
            return True
        if current_position[0] > self.dimension_maze[0] or current_position[1] > self.dimension_maze[1] or current_position[0] < 0 or (current_position[1] < 0):
            return False
        if self.maze[current_position[0]][current_position[1]] == 'W':
            return False
        else:
            down = (current_position[0] + 1, current_position[1])
            up = (current_position[0] - 1, current_position[1])
            rigth = (current_position[0], current_position[1] + 1)
            left = (current_position[0], current_position[1] - 1)
            new_positions = [down, up, rigth, left]
            path_find = False
            for position in new_positions:
                if position not in self.previous_positions:
                    self.previous_positions.append(position)
                    path_find = path_find or self.recursive_path(position)
        return path_find
