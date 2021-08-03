import numpy as np
from numba import njit
i8 = np.int64


@njit
def solve(a, b, t, K, N):
    t1 = t // K
    d = t % K * 2
    # b が a から a + d の位置にあれば衝突する
    x = 0
    y = 0
    ans = 0
    for c in a:
        while b[x] < c:
            x += 1
        while b[y] <= c + d:
            y += 1
        ans += y - x
    ans += t1 * len(a) * (N - len(a)) * 2
    return ans


def set_ini(DX, K):
    a = DX[1][DX[0] == 1]
    a = np.sort(a)
    b = DX[1][DX[0] == 2]
    b = np.sort(b)
    b = np.hstack((b, b + K, b + 2 * K, [3 * K]))
    return a, b


def main():
    f = open('/dev/stdin', 'rb')
    vin = np.fromstring(f.read(), i8, sep=' ')
    N, Q, K = vin[0:3]
    head = 3
    DX = vin[head:head + 2 * N].reshape(-1, 2).T
    a, b = set_ini(DX, K)
    head += 2 * N
    T = vin[head: head + Q]
    for t in T:
        print(solve(a, b, t, K, N))


def __starting_point():
    main()


__starting_point()
