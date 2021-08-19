import sys
import bisect
import collections

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    UV = [[int(x) for x in input().split()] for _ in range(N - 1)]

    T = [[] for j in range(N + 1)]

    for u, v in UV:
        T[u].append(v)
        T[v].append(u)

    s = collections.deque()

    lis = []
    s.append([1, lis])

    v = set()

    ans = [0] * (N + 1)
    memo = [[] for j in range(N + 1)]

    while s:
        c = s[-1]
        ci, clis = c[0], c[1]

        # lis処理
        if ci not in v:
            if len(clis) == 0:
                clis.append(A[ci - 1])
                memo[ci].append(-1)
            else:
                if clis[-1] < A[ci - 1]:
                    clis.append(A[ci - 1])
                    memo[ci].append(-1)
                else:
                    i = bisect.bisect_left(clis, A[ci - 1])
                    memo[ci].append(i)
                    memo[ci].append(clis[i])
                    clis[i] = A[ci - 1]

            v.add(ci)
            ans[ci] = len(clis)

        if len(T[ci]) >= 1:
            n = T[ci].pop()
            if n in v:
                continue
            s.append([n, clis])
            continue

        if memo[ci][0] == -1:
            if len(clis) >= 1:
                clis.pop()
        else:
            clis[memo[ci][0]] = memo[ci][1]

        s.pop()

    for i in range(1, N + 1):
        print((ans[i]))


def __starting_point():
    main()


__starting_point()
