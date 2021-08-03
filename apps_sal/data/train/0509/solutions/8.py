# See. https://atcoder.jp/contests/arc108/tasks/arc108_c

import numpy as np


def solve(N, G):
    q = np.zeros(N, dtype=np.uint32)
    q[0] = 1

    labels = np.zeros(N + 1, dtype=np.uint32)
    labels[1] = 1
    end = 1

    for head in range(N):
        u = q[head]
        if u < 1:
            break
        for v in list(G[u].keys()):
            if labels[v] > 0:
                continue
            labels[v] = G[u][v] if labels[u] != G[u][v] else labels[u] % N + 1
            q[end] = v
            end += 1
    else:
        return labels[1:]

    return ['No']


def main():
    N, M = [int(x) for x in input().split()]
    G = {}
    for i in range(M):
        u, v, c = [int(x) for x in input().split()]

        for u_, v_ in ((u, v), (v, u)):
            if u_ not in G:
                G[u_] = {}
            G[u_][v_] = c

    ans = solve(N, G)
    for i in range(len(ans)):
        print((ans[i]))


main()

# vim: ts=2 sw=2
