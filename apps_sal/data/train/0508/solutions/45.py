from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def N():
    return int(input())


def NM():
    return map(int, input().split())


def L():
    return list(NM())


def LN(n):
    return [N() for i in range(n)]


def LL(n):
    return [L() for i in range(n)]


def YesNo(x):
    print('Yes') if x == True else print('No')


(n, q) = NM()
l = []
for i in range(n):
    (s, t, x) = NM()
    l.append((s - x, t - x, x))
l.sort()
INF = float('inf')
l += [(INF, INF, INF)]
d = LN(q)
q = []
j = 0
for i in d:
    while l[j][0] <= i:
        (s, t, x) = l[j]
        heappush(q, (x, t))
        j += 1
    if len(q) == 0:
        print(-1)
    else:
        while q:
            (x, t) = heappop(q)
            if t > i:
                heappush(q, (x, t))
                print(x)
                break
        else:
            print(-1)
