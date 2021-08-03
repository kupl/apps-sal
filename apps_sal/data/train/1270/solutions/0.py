import sys
sys.setrecursionlimit(100000)

memo = {}


def recurse(arr, T1, T2, k, i):
    if T1 >= k and T2 >= k:
        return i

    if i >= len(arr):
        return float('inf')

    if (T1, T2) in memo:
        return memo[(T1, T2)]

    t1 = recurse(arr, T1 + arr[i], T2, k, i + 1)
    t2 = recurse(arr, T1, T2 + arr[i], k, i + 1)

    memo[(T1, T2)] = min(t1, t2)
    return memo[(T1, T2)]


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    lst = list(map(int, input().split()))

    lst.sort(reverse=True)
    memo = {}
    res = recurse(lst, 0, 0, k, 0)

    if res == float('inf'):
        print(-1)
    else:
        print(res)
