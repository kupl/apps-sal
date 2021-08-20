import sys


def solve():
    (N, D) = list(map(int, sys.stdin.readline().split()))
    A = list(map(int, sys.stdin.readline().split()))
    V = None
    M = 0
    for i in range(D):
        X = A[i::D]
        if sum(X) % len(X) != 0:
            return -1
        v = sum(X) / len(X)
        if V and V != v:
            return -1
        for i in range(len(X)):
            c = X[i] - v
            M += abs(v - X[i])
            if i < len(X) - 1:
                X[i + 1] += c
    return M


T = int(sys.stdin.readline())
for _ in range(T):
    print(solve())
