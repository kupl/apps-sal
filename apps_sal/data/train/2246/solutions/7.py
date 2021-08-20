import heapq


def process(n, k, X, a, C):
    res = 0
    A = []
    for i in range(len(X)):
        heapq.heappush(A, C[i])
        if k + len(A) * a < X[i]:
            return -1
        else:
            while k < X[i]:
                res += heapq.heappop(A)
                k += a
    return res


(n, k) = [int(x) for x in input().split()]
X = [int(x) for x in input().split()]
a = int(input())
C = [int(x) for x in input().split()]
print(process(n, k, X, a, C))
