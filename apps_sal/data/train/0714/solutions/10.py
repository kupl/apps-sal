import math
t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    v = math.ceil(sum(lst) / n)
    b = 0
    t = 0
    for i in lst:
        if i > v:
            b += i - v
    t += b
    for i in lst:
        if i < v:
            b -= v - i
            i += v - i
    t += abs(b)
    print(t)
