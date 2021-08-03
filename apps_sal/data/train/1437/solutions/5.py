# cook your dish here
import math
for _ in range(int(input())):
    input()
    l = list(map(int, input().split(" ")))
    l.sort()
    i = 0
    j = len(l) - 1
    n = -1
    f = True
    while i <= j:
        if i == 0:
            n = l[i] * l[j]
        elif l[i] * l[j] != n:
            f = False
            break
        i += 1
        j -= 1

    j = len(l)
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            if n // i == i:
                j -= 1
            else:
                j -= 2

    if f and j == 0:
        print(n)
    else:
        print(-1)
