def bs1(arr, x):
    low = 0
    high = len(arr) - 1
    p = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] < x:
            p = mid
            low = mid + 1
        else:
            high = mid - 1
    if arr[p] <= x:
        return arr[p]
    else:
        return 0


def bs2(arr, x):
    low = 0
    high = len(arr) - 1
    p = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] < x:
            low = mid + 1
        else:
            p = mid
            high = mid - 1
    if arr[p] >= x:
        return arr[p]
    else:
        return 1000000


(n, a, b) = list(map(int, input().strip().split()))
s = []
e = []
for i in range(n):
    (c, d) = list(map(int, input().strip().split()))
    s.append(c)
    e.append(d)
ws = list(map(int, input().strip().split()))
vs = list(map(int, input().strip().split()))
ws.sort()
vs.sort()
r = 1000000
for i in range(n):
    s1 = bs1(ws, s[i])
    e1 = bs2(vs, e[i])
    r1 = e1 - s1 + 1
    if r1 < r:
        r = r1
print(r)
