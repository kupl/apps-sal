import sys
input = sys.stdin.readline
(inp, ip) = (lambda: int(input()), lambda: [int(w) for w in input().split()])
for _ in range(inp()):
    n = inp()
    x = [1 for i in range(n)]
    print(*x)
