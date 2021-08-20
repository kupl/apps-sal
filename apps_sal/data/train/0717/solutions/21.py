import math
for _ in range(int(input())):
    (a, b) = map(int, input().split())
    if a == b:
        print(a * a)
    else:
        print((a + b - 1) * 2)
