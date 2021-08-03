# cook your dish here
import math
for _ in range(int(input())):
    n = int(input())
    x = 0
    for i in range(n):
        l = list(map(int, input().split()))
        c = l[0]
        l1 = l[1:]
        s = len(l1)
        d = math.ceil(s / 2)
        for i in range(d):
            x = x + l1[i]
    print(x)
