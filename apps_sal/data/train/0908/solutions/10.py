from math import sqrt
itr = int(input())
for i in range(itr):
    n = int(input())
    j = int(sqrt(n * 2))
    while (j > 0):
        if (j * (j + 1) / 2) <= n:
            print(j)
            break
        j -= 1
