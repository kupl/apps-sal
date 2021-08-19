import math
n = int(input())
for i in range(n):
    (a, b) = list(map(int, input().split()))
    if a > b:
        a1 = math.ceil(a / (2 * b))
        b1 = a - a1 * b
        a2 = math.floor(a / (2 * b))
        b2 = a - a2 * b
        print(max(a1 * b1, a2 * b2))
    else:
        print(0)
