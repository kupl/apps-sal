import sys
[n, q] = map(int, sys.stdin.readline().strip().split())
qis = [int(sys.stdin.readline().strip()) for _ in range(q)]


def query(n, q):
    d = 2 * n - q
    while d % 2 == 0:
        d //= 2
    return n - d // 2


for qi in qis:
    print(query(n, qi))
