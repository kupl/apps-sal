import sys
t = eval(input())
for _ in range(t):
    s = list(map(str, sys.stdin.readline().split()))[0]
    n = len(s)
    d = {}
    for i in range(1, n):
        k = s[i - 1:i + 1]
        if k not in d:
            d[k] = 0
    print(len(list(d.keys())))
