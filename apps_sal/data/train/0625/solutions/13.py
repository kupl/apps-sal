import collections


def subarraysDivByK(A, K):
    P = [0]
    for x in A:
        P.append((P[-1] + x) % K)

    count = collections.Counter(P)
    return sum(v * (v - 1) / 2 for v in count.values())


t = int(input())
for _ in range(t):
    n = int(input())
    arr = map(int, input().split())
    print(int(subarraysDivByK(arr, 1000000000)))
