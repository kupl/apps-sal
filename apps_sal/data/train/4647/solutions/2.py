def get_neighbourhood(n_type, matrix, coordinates):
    height = len(matrix)
    width = len(matrix[0])
    (y, x) = coordinates
    if not (0 <= y < height and 0 <= x < width):
        return []
    moore = [(y + dy, x + dx) for dy in [-1, 0, 1] for dx in [-1, 0, 1] if (dy, dx) != (0, 0)]
    von_neumann = [moore[idx] for idx in (1, 3, 4, 6)]
    neighbors_coords = eval(n_type)
    neighbors = [matrix[y][x] for (y, x) in neighbors_coords if 0 <= y < height and 0 <= x < width]
    return neighbors
