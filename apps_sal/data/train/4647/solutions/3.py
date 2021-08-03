D = {"von_neumann": ((0, 1), (0, -1), (1, 0), (-1, 0)),
     "moore": ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))}


def get_neighbourhood(n_type, mat, coordinates):
    (i, j), H, W = coordinates, len(mat), len(mat[0])
    def check(a, b): return 0 <= i + a < H and 0 <= j + b < W
    return [mat[i + k][j + l] for k, l in D[n_type] if check(k, l)] if check(0, 0) else []
