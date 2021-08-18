from bisect import bisect_left, bisect_right
import sys
sys.setrecursionlimit(10**8)
N = int(input())
a = list(map(int, input().split()))
lists = [[] for i in range(N)]
for i in range(N - 1):
    u, v = map(int, input().split())
    lists[u - 1].append(v - 1)
    lists[v - 1].append(u - 1)


def search(v, LIS):
    if len(lists[v]) == 0:
        return
    for u in lists[v]:
        if check[u] == False:
            check[u] = True
            if a[u] > LIS[-1]:
                LIS.append(a[u])
                ans[u] = len(LIS)
                search(u, LIS)
                LIS.pop()
            else:
                ind = bisect_left(LIS, a[u])
                stack = LIS[ind]
                LIS[ind] = a[u]
                ans[u] = len(LIS)
                search(u, LIS)
                LIS[ind] = stack
    return


ans = [0] * N
check = [False] * N
check[0] = True
LIS = [a[0]]
ans[0] = 1
search(0, LIS)
print(*ans, sep="\n")
