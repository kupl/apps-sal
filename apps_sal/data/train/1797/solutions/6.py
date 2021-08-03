from heapq import *

H, Q = [1], [(2, 2, 1), (3, 3, 1), (5, 5, 1)]


def hamming(n):
    while len(H) <= n:
        v, root, i = heappop(Q)
        if H[-1] != v:
            H.append(v)
        heappush(Q, (H[i] * root, root, i + 1))
    return H[n - 1]
