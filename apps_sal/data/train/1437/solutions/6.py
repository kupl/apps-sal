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
            if list[j] != vec[it]:
                return -1
            else:
                j += 1
    return x


try:
    m = int(input())
    for i in range(m):
        n = int(input())
        x = list(map(int, input().split()))
        print(findX(x, n))
except EOFError as e:
    print(e)
