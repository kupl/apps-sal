from bisect import bisect_left


def performant_smallest(arr, n):
    sarr = sorted(arr)
    limit = sarr[n - 1]
    r = n - bisect_left(sarr, limit)
    ans = []
    for a in arr:
        if a < limit or (a == limit and r):
            ans.append(a)
            r -= a == limit
            if len(ans) == n:
                return ans
