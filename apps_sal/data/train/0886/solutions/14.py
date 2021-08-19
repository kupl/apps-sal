# cook your dish here
import bisect
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    for i in range(n):
        mod = arr[i] % 3
        arr[i] = arr[i] + mod
    arr = sorted(arr)
    idx = bisect.bisect(arr, m)
    if idx == 0:
        if arr[0] > m:
            g = arr[0]
        else:
            g = arr[1]
        s = -1
    elif idx == n:
        if arr[n - 1] < m:
            s = arr[n - 1]
        else:
            s = arr[n - 2]
        g = -1
    else:
        s = arr[idx - 1]
        if s == m:
            if idx - 2 < 0:
                s = -1
            else:
                s = arr[idx - 2]
        g = arr[idx]
        if g == m:
            if idx + 1 > n - 1:
                g = -1
            else:
                g = arr[idx + 1]
    print(s, g)
