import math


def findX(list, int):
    list.sort()
    x = list[0] * list[int - 1]
    vec = []
    i = 2
    while i * i <= x:
        if x % i == 0:
            vec.append(i)
            if x // i != i:
                vec.append(x // i)
        i += 1
    vec.sort()
    if len(vec) != int:
        return -1
    else:
        j = 0
        for it in range(int):
            if a[j] != vec[it]:
                return -1
            else:
                j += 1
    return x


t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    print(findX(a, n))
