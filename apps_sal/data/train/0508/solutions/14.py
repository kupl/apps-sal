import sys
from heapq import *
input = sys.stdin.readline


def main():
    n, q = map(int, input().split())

    key = []
    for i in range(n):
        s, t, x = map(int, input().split())
        l, r = max(0, s - x), max(0, t - x)
        key.append((l, -1, x))
        key.append((r, 1, x))

    key.sort()
    judge = []
    already = dict()
    search = []

    for i in range(n * 2):
        s, j, x = key[i]

        if j == -1:
            heappush(judge, x)
        else:
            if x in already:
                already[x] += 1
            else:
                already[x] = 1

        if i == n * 2 - 1 or key[i][0] != key[i + 1][0]:
            while judge:
                if judge[0] in already and already[judge[0]] > 0:
                    already[judge[0]] -= 1
                    heappop(judge)
                else:
                    break
            if judge:
                search.append((s, judge[0]))
            else:
                search.append((s, -1))

    size = len(search)
    index = 0
    answer = []
    for i in range(q):
        d = int(input())
        while index < size - 1:
            if search[index + 1][0] <= d:
                index += 1
            else:
                break
        print(search[index][1])


def __starting_point():
    main()


__starting_point()
