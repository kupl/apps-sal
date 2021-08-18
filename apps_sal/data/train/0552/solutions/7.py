import heapq


def kSmallest(lst, k, n):
    res = lst[:k]
    heapq._heapify_max(res)
    for i in range(k, n):
        if lst[i] < res[0]:
            heapq._heapreplace_max(res, lst[i])
    return res


def solve():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        k = min(k, n - k)
        a = [int(x) for x in input().split()]
        b = kSmallest(a, k, n)
        print(abs(sum(a) - 2 * sum(b)))


solve()
