# cook your dish here
from math import factorial
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    x = 0
    y = 0
    if k > 0:
        for j in range(n):
            if l[j] == l[k - 1] and j < k:
                x += 1
            elif l[j] == l[k - 1] and j >= k:
                y += 1
            elif l[j] > l[k - 1]:
                break
        s = int((factorial(x + y)) // ((factorial(x)) * factorial(y)))
        print(s)
    else:
        print(1)
