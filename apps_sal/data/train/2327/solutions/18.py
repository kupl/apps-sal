"""
BIT
区間[L,R]にxを加える。
座標Xでの値を求める。
"""
import sys
input = sys.stdin.readline


def bit_add(i, x):
    while i <= M:
        tree[i] += x
        i += i & -i


def bit_sum(i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & -i
    return s


(N, M) = map(int, input().split())
data = []
for i in range(N):
    (l, r) = map(int, input().split())
    data.append([r - l, l, r])
data.sort()
k = 0
tree = [0] * (M + 1)
for d in range(1, M + 1):
    while k < N and data[k][0] < d:
        bit_add(data[k][1], 1)
        bit_add(data[k][2] + 1, -1)
        k += 1
    ans = 0
    for j in range(1, M // d + 1):
        ans += bit_sum(d * j)
    print(ans + N - k)
