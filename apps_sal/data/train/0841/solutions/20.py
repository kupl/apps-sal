from operator import mul

M = 10 ** 9 + 7
N = 100001

p10 = [None] * N
p10[0] = 1
for i in range(1, N):
    p10[i] = p10[i - 1] * 10 % M

t = int(input())
for _ in range(t):
    s = list(map(int, input()))
    p = sum(map(mul, reversed(s), p10))
    m = p10[len(s)]
    r = 0
    for d in s:
        r = (r * m + p) % M
        p = (p * 10 - (m - 1) * d) % M
    print(r)
