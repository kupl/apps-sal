import sys

R = lambda t = int: t(eval(input()))
RL = lambda t = int: [t(x) for x in input().split()]
RLL = lambda n, t = int: [RL(t) for _ in range(n)]

def solve():
    p, q, r = RL()
    a, b, c = RL()
    if p > a or q > b or r > c:
        print(-1)
        return
    print(a-p+b-q+c-r)

T = R()
for t in range(1, T + 1):
    solve()

