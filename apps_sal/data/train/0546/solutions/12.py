import math
T = int(input())
for _ in range(T):
    D = int(input())
    count = 0
    while D > 0:
        p = int(math.log(D, 2))
        D = D - 2 ** p
        count += 1
    print(count - 1)
