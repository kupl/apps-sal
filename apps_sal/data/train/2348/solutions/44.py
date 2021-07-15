from collections import deque
from bisect import bisect_right, bisect_left

N = int(input())
x = list(map(int, input().split()))
L = int(input())

K = 0
tmp = 1
while tmp <= N:
    tmp *= 2
    K += 1

parent = [[None] * N for _ in range(K)]
parent[0][N-1] = N-1
for i in range(N-1):
    d = bisect_right(x, x[i] + L)
    parent[0][i] = d-1

# print(parent[0])
#     print(depth)

for k in range(1, K):
    for i in range(N):
        parent[k][i] = parent[k - 1][parent[k - 1][i]]

# print(parent)

Q = int(input())
for _ in range(Q):
    ans = 0
    a, b = [int(x)-1 for x in input().split()]
    if a > b:
        a, b = b, a
    # print(a, b)
    for i in range(K - 1, -1, -1):
        if parent[i][a] < b:
            a = parent[i][a]
            ans += pow(2, i)
    print((ans+1))

