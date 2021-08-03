import sys
from heapq import *
input = sys.stdin.readline


def main():
    n, q = list(map(int, input().split()))

    key = []
    for i in range(n):
        s, t, x = list(map(int, input().split()))
        l, r = max(0, s - x), max(0, t - x)
        key.append((l, 1, x))
        key.append((r, -1, x))

    for i in range(q):
        d = int(input())
        key.append((d, 2))

    key.sort()
    judge = []
    already = dict()

    for i in range(2 * n + q):
        k = key[i]
        if k[1] == -1:
            if k[2] in already:
                already[k[2]] += 1
            else:
                already[k[2]] = 1
        elif k[1] == 1:
            heappush(judge, k[2])
        else:
            while judge:
                if judge[0] in already and already[judge[0]] > 0:
                    already[judge[0]] -= 1
                    heappop(judge)
                else:
                    break
            if judge:
                print((judge[0]))
            else:
                print((-1))


def __starting_point():
    main()


__starting_point()
