for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    indexOf = {}
    for i in range(n):
        indexOf[a[i]] = i
    values = sorted(list(set(a)))
    visited = [False for _ in range(n)]
    ng = [n for _ in range(n)]
    for i in range(n):
        lo = 0
        hi = len(values)-1
        while lo < hi:
            mid = (lo + hi) // 2
            if values[mid] < a[i]:
                lo = mid + 1
            else:
                hi = mid
        if lo != len(values) - 1:
            ng[i] = indexOf[values[lo+1]]
    ans = n
    for i in range(n):
        if visited[i]:
            continue
        tempAns = n
        at = i
        while at != n:
            visited[at] = True
            tempAns -= 1
            if ng[at] > at:
                at = ng[at]
            else:
                at = n
        ans = min(ans, tempAns)
    print(ans)

