import sys


def solve(x_s: int, y_s: int, x_t: int, y_t: int, N: int, x: 'List[int]', y: 'List[int]', r: 'List[int]'):
    import numpy as np
    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph import dijkstra
    x.extend([x_s, x_t])
    y.extend([y_s, y_t])
    r.extend([0, 0])
    p = np.column_stack((x, y))
    diff = np.expand_dims(p, axis=1) - np.expand_dims(p, axis=0)
    dist = np.sqrt(np.sum(diff ** 2, axis=-1))
    delta = 0.5
    mat = csr_matrix(((dist - r).T - r).clip(min=0) - delta)
    mat.data += delta
    return dijkstra(mat, indices=N)[N + 1]


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x_s = int(next(tokens))
    y_s = int(next(tokens))
    x_t = int(next(tokens))
    y_t = int(next(tokens))
    N = int(next(tokens))
    x = [int()] * N
    y = [int()] * N
    r = [int()] * N
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        r[i] = int(next(tokens))
    print(solve(x_s, y_s, x_t, y_t, N, x, y, r))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
