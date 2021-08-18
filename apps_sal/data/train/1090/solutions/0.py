
import collections


def shortestSubarray(A, K):

    N = len(A)
    P = [0]

    for x in A:
        P.append(P[-1] + x)

    ans = N + 1
    monoq = collections.deque()
    for y, Py in enumerate(P):
        if not monoq:
            if Py >= K:
                return 1
        while monoq and Py <= P[monoq[-1]]:
            monoq.pop()

        while monoq and Py - P[monoq[0]] >= K:
            ans = min(ans, y - monoq.popleft())

        monoq.append(y)

    return ans if ans < N + 1 else -1


for t in range(int(input())):
    N, D = [int(x) for x in input().split()]

    A = [int(x) for x in input().split()]

    print(shortestSubarray(A, D))
