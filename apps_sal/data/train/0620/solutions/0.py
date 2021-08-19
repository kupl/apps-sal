for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    def check(mid):
        d, left = {}, 0
        for i in range(mid):
            if a[i] > k:
                if a[i] not in d:
                    d[a[i]] = 1
                else:
                    d[a[i]] += 1
        if len(d) == 1:
            return True
        for i in range(mid, n):
            if a[left] > k:
                d[a[left]] -= 1
                if d[a[left]] == 0:
                    del d[a[left]]
            if a[i] > k:
                if a[i] not in d:
                    d[a[i]] = 1
                else:
                    d[a[i]] += 1
            if len(d) == 1:
                return True
            left += 1
        return False

    lo, hi = 0, n
    while lo <= hi:
        mid = (lo + hi) // 2
        # print(mid,lo,hi)
        if check(mid):
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(res)
