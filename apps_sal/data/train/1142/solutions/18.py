# cook your dish here
from bisect import insort
try:
    x = []
    for _ in range(int(input())):
        t = int(input())
        insort(x, t)
        x.sort(reverse=True)
        print(x.index(t) + 1)
except:
    pass
