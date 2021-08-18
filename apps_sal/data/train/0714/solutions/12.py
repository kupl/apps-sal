import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    x = sum(a)
    b = math.ceil(x / len(a))
    op = ((b * len(a)) - x)
    for i in range(len(a)):
        if a[i] >= b:
            op += (a[i] - b)
    print(op)
