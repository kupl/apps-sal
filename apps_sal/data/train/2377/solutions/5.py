import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    c = {}
    for i in range(n - 1):
        c[b[i + 1]] = b[i]
    c[b[0]] = -1
    li = {}
    for i in a:
        if c[i] in li:
            li[i] = li[c[i]] + 1
        else:
            li[i] = 1
    print(n - max(li.values()))
