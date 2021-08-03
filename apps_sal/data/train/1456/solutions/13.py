import math


def count(N):
    if(N < 1):
        return 0
    total = N * (N + 1) // 2
    a = 1
    d = 2
    while(N >= a):
        n = math.floor((N - a) / d) + 1
        total -= (n * a + 1)
        a *= 2
        d *= 2
    return total


T = int(input())
for _ in range(T):
    L, R = list(map(int, input().split()))
    print(count(R) - count(L - 1))
