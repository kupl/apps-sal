import sys
input = sys.stdin.readline
inp, ip = lambda: int(input()), lambda: [int(w) for w in input().split()]

for _ in range(inp()):
    s = input().strip()
    dt = {}
    for i in s:
        dt[i] = dt.get(i, 0) + 1
    print(len(dt))
