import math
from functools import reduce


def printDivisors(n):
    return list(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))


for _ in range(int(input())):
    N = int(input())
    List = [int(y) for y in input().split()]
    Dict = dict()
    Answ = 0
    for i in range(N):
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
