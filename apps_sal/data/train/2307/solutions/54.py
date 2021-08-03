import sys
input = sys.stdin.readline


def read():
    N, A, B = list(map(int, input().strip().split()))
    X = list(map(int, input().strip().split()))
    return N, A, B, X


def solve(N, A, B, X):
    ans = 0
    for i in range(N - 1):
        d = X[i + 1] - X[i]
        ans += min(A * d, B)
    return ans


def __starting_point():
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print(("%s" % str(outputs)))


__starting_point()
