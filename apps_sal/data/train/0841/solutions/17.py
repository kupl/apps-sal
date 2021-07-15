from operator import mul

M = 10 ** 9 + 7
N = 100001

p10 = [None] * N
k = 1
for i in range(N):
    p10[i] = k
    k = k * 10 % M 

t = int(input())
for _ in range(t):
    s = list(map(int, input()))
    m = p10[len(s)]
    p = sum(map(mul, reversed(s), p10))
    r = 0
    for d in s:
        r = (r * m + p) % M
        p = (p * 10 - (m - 1) * d) % M
    print(r)

