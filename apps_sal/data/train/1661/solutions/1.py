import re


def execute(code):

    def simplify_code(code):
        while '(' in code:
            code = re.sub('\\(([^()]*)\\)(\\d*)', lambda match: match.group(1) * int(match.group(2) or 1), code)
        code = re.sub('([FLR])(\\d+)', lambda match: match.group(1) * int(match.group(2)), code)
        return code

    def compute_path(simplified_code):
        (pos, dir) = ((0, 0), (1, 0))
        path = [pos]
        for cmd in simplified_code:
            if cmd == 'F':
                pos = tuple((a + b for (a, b) in zip(pos, dir)))
                path.append(pos)
            elif cmd == 'L':
                dir = (dir[1], -dir[0])
            elif cmd == 'R':
                dir = (-dir[1], dir[0])
        return path

    def compute_bounding_box(path):
        min_x = min((pos[0] for pos in path))
        min_y = min((pos[1] for pos in path))
        max_x = max((pos[0] for pos in path))
        max_y = max((pos[1] for pos in path))
        return ((min_x, min_y), (max_x, max_y))

    def build_grid(path):
        (min_xy, max_xy) = compute_bounding_box(path)
        width = max_xy[0] - min_xy[0] + 1
        height = max_xy[1] - min_xy[1] + 1
        grid = [[' '] * width for _ in range(height)]
        for (x, y) in path:
            grid[y - min_xy[1]][x - min_xy[0]] = '*'
        return grid

    def grid_to_string(grid):
        return '\r\n'.join((''.join(row) for row in grid))
    code = simplify_code(code)
    path = compute_path(code)
    grid = build_grid(path)
    return grid_to_string(grid)
