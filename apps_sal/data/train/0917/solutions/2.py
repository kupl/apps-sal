from collections import *
for u in range(int(input())):
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    d = []
    x = 100000000000000
    for i in range(n - 1):
        for j in range(i + 1, n):
            x = min(x, abs(l[i] + l[j] - k))
            d.append(abs(l[i] + l[j] - k))
    print(x, d.count(x))
