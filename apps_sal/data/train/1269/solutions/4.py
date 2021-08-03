import itertools
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    b.sort()
    s = 0
    for (f, g) in zip(a, b):
        s += min(f, g)
    print(s)
