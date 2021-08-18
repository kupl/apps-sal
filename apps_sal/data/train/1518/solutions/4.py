import sys
import math
T = int(input())


def is_prime(x):
    for j in range(2, int(math.sqrt(x)) + 1):
        if x % j == 0:
            return 0
    return 1


for t in range(T):
    row = list(int(x) for x in input().split())
    N = row[0]
    K = row[1]
    if K == 1:
        print(is_prime(N))
    elif K == 2 and N >= 4:
        if N % 2 == 0:
            print(1)
        else:
            print(0)
    elif K >= 3 and N >= 2 * K:
        print(1)
    else:
        print(0)
