from scipy.sparse.csgraph import csgraph_from_dense, dijkstra
import numpy as np
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


def main():
    (x_s, y_s, x_t, y_t) = list(map(int, readline().split()))
    A = np.array([[x_s, y_s, 0], [x_t, y_t, 0]], dtype=np.int)
    N = int(readline())
    B = np.array(read().split(), dtype=np.int).reshape(-1, 3)
    (XY, R) = np.hsplit(np.concatenate((A, B)), [2])
    d = np.expand_dims(XY, axis=1) - np.expand_dims(XY, axis=0)
    d = np.sqrt(np.sum(d ** 2, axis=-1))
    d -= R + R.reshape(1, -1)
    d = np.maximum(d, 0)
    np.fill_diagonal(d, -1)
    d = csgraph_from_dense(d, null_value=-1)
    ans = dijkstra(d, indices=0)[1]
    print(ans)


def __starting_point():
    main()


__starting_point()
