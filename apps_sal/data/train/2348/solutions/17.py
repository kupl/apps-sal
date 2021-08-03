from bisect import bisect_right
import sys
input = sys.stdin.readline
n = int(input())
X = tuple(map(int, input().split()))
l = int(input())
q = int(input())
D = [[0] * n for _ in range(18)]
for i in range(n):
    D[0][i] = bisect_right(X, X[i] + l) - 1
for k in range(1, 18):
    for i in range(n):
        D[k][i] = D[k - 1][D[k - 1][i]]


def query(a, b):
    ret = 0
    while True:
        for k in range(18):
            if D[k][a] >= b:
                break
        if k == 0:
            ret += 1
            return ret
        k -= 1
        ret += pow(2, k)
        a = D[k][a]


for _ in range(q):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    a -= 1
    b -= 1
    print(query(a, b))
