import sys
input = sys.stdin.readline
(inp, ip) = (lambda: int(input()), lambda: [int(w) for w in input().split()])
for _ in range(inp()):
    n = inp()
    ans = []
    t = 10 ** 5 - 2
    for i in range(n // t):
        ans.extend([t + 2, t + 1, 1])
    n = n % t
    ans.extend([n + 2, n + 1, 1])
    print(len(ans))
    print(*ans)
