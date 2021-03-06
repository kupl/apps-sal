import sys
from collections import deque
inf = float('inf')


def solve(N: int, a: 'List[int]', b: 'List[int]'):
    adj = [set() for _ in range(N)]
    for (u, v) in zip(a, b):
        adj[u].add(v)
        adj[v].add(u)
    dist_F = [inf for _ in range(N)]
    dist_F[0] = 0
    dist_S = [inf for _ in range(N)]
    dist_S[N - 1] = 0
    Q = deque([(0, 0)], N)
    while len(Q) > 0:
        (du, u) = Q.pop()
        for v in adj[u]:
            if dist_F[v] < inf:
                continue
            dist_F[v] = du + 1
            Q.append((du + 1, v))
    Q = deque([(0, N - 1)], N)
    while len(Q) > 0:
        (du, u) = Q.pop()
        for v in adj[u]:
            if dist_S[v] < inf:
                continue
            dist_S[v] = du + 1
            Q.append((du + 1, v))
    c_S = 0
    c_F = 0
    for (df, ds) in zip(dist_F, dist_S):
        if df <= ds:
            c_F += 1
        else:
            c_S += 1
    if c_F <= c_S:
        print('Snuke')
    else:
        print('Fennec')
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    a = [int()] * (N - 1)
    b = [int()] * (N - 1)
    for i in range(N - 1):
        a[i] = int(next(tokens)) - 1
        b[i] = int(next(tokens)) - 1
    solve(N, a, b)


def __starting_point():
    main()


__starting_point()
