def get_neighbourhood(n_type, mat, coordinates):
    d = {'moore': [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, -1), (1, 1), (-1, -1)], 'von_neumann': [(0, 1), (1, 0), (-1, 0), (0, -1)]}
    (y, x) = coordinates
    if not mat or not 0 <= y < len(mat) or (not 0 <= x < len(mat[0])):
        return []
    r = []
    for (i, j) in d.get(n_type):
        (a, b) = (y + i, x + j)
        if 0 <= a < len(mat) and 0 <= b < len(mat[0]):
            r.append(mat[a][b])
    return r
