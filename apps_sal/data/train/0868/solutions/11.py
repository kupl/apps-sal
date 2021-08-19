import math
from bisect import bisect_left


def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    else:
        return False


for _ in range(int(input())):
    ans = 0
    (N, k) = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    for i in range(N):
        for j in range(i, N):
            S = a[i:j + 1]
            S.sort()
            god = math.ceil(k / len(S))
            X = S[math.ceil(k / god) - 1]
            F = 0
            for z in S:
                if z == X:
                    F += 1
            if BinarySearch(S, F):
                ans += 1
    print(ans)
