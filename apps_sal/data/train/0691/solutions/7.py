import math
from functools import reduce


def printDivisors(n):
    return list(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))


for _ in range(int(input())):
    n = int(input())
    if n > 10 ** 4:
        List = [int(y) for y in input().split()]
        Dict = dict()
        Answ = 0
        for i in range(n):
            Divisor_List = printDivisors(List[i])
            if List[i] in Dict:
                if Dict[List[i]] > Answ:
                    Answ = Dict[List[i]]
            for i in Divisor_List:
                if i in Dict:
                    Dict[i] += 1
                else:
                    Dict[i] = 1
        print(Answ)
    else:
        a = list(map(int, input().split()))
        h = [0] * 1000001
        m = 0
        for j in range(n - 1, 1, -1):
            x = j - 1
            c = 0
            if h[a[j]] == 0:
                while x >= 0:
                    if a[x] % a[j] == 0:
                        h[a[x]] = 1
                        c = c + 1
                    x = x - 1
                m = max(m, c)
                h[a[j]] = 1
        print(m)
