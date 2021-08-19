import math
t = int(input())
for i in range(t):
    b = []
    n = int(input())
    for p in range(n + 1, 2 * n):
        if p % 2 == 0:
            a = math.sqrt(n ** 2 - (p / 2) ** 2)
            if a - int(a) == 0:
                b.append(i)
    if len(b) == 0:
        print('NO')
    elif len(b) != 0:
        print('YES')
