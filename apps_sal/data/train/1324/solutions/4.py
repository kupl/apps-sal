import math


def find_fac(fac, n):
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n // i != i:
                fac.append(n // i)
            fac.append(i)


for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    temp = (k * (k + 1)) // 2
    fac = []
    find_fac(fac, n)
    fac.sort()
    flag = 0
    for i in range(len(fac) - 1, -1, -1):
        if (n // fac[i]) >= temp:
            break
        flag += 1
    if flag == len(fac):
        print(-1)
    else:
        print(fac[i])
