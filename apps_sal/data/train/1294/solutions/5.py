import sys
import collections
input = sys.stdin.readline


def main1():
    T = int(input())
    for _ in range(T):
        (N, K) = map(int, input().split())
        Tree = {}
        for j in range(N):
            Tree[j] = []
        for i in range(N - 1):
            (u, v) = map(int, input().split())
            Tree[u - 1].append(v - 1)
            Tree[v - 1].append(u - 1)
        A = list(map(int, input().split()))
        vis = [0 for i in range(N)]
        maxval = [[0, 0] for i in range(N)]
        minval = [0 for i in range(N)]
        lfnode = []
        vis[0] = 1
        Q = collections.deque([0])
        (maxval[0][0], maxval[0][1]) = (A[0], 1)
        minval[0] = A[0]
        while len(Q) != 0:
            a = Q.pop()
            mv1 = maxval[a][0]
            mv2 = minval[a]
            flag = 0
            for i in Tree[a]:
                if vis[i] == 0:
                    vis[i] = 1
                    flag = 1
                    v = A[i]
                    Q.append(i)
                    if mv1 < v:
                        (maxval[i][0], maxval[i][1]) = (v, 1)
                    elif mv1 == v:
                        (maxval[i][0], maxval[i][1]) = (mv1, maxval[a][1] + 1)
                    else:
                        (maxval[i][0], maxval[i][1]) = (maxval[a][0], maxval[a][1])
                    if mv2 > v:
                        minval[i] = v
                    elif v == mv2:
                        minval[i] = mv2
                    else:
                        minval[i] = minval[a]
            if flag == 0:
                lfnode.append(a)
        flag = 0
        K1 = len(bin(K)) - 2
        for i in lfnode:
            (v1, v2) = (maxval[i][0], maxval[i][1])
            if v1 > K1 and v2 % 2 == 0:
                flag = 1
            elif v1 == K1 and v2 % 2 == 1:
                flag = 1
            v11 = minval[i]
            if v11 > K1 and v11 != v1:
                flag = 1
            elif v11 == K1:
                flag = 1
            if flag == 1:
                break
        if flag == 1:
            print('YES')
        else:
            print('NO')


main1()
