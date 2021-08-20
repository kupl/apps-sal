def can(d, a, b):
    d1 = d
    mi = a[-1]
    ma = a[-1]
    x = len(a) - 1
    y = len(b) - 1
    while x >= 0 and y >= 0:
        if b[y] <= mi:
            if abs(b[y] - ma) <= d1:
                x -= 1
                if x == -1:
                    break
                ma = a[x]
            else:
                y -= 1
                mi = a[x]
                ma = a[x]
        elif b[y] >= ma:
            if abs(b[y] - mi) <= d1:
                x -= 1
                if x == -1:
                    break
                ma = a[x]
            else:
                y -= 1
                mi = a[x]
                ma = a[x]
        elif abs(ma - mi) + min(abs(b[y] - mi), abs(b[y] - ma)) <= d1:
            x -= 1
            if x == -1:
                break
            ma = a[x]
        else:
            y -= 1
            mi = a[x]
            ma = a[x]
    return x == -1


(n, m) = list(map(int, input().split()))
s = list(map(int, input().split()))[::-1]
s1 = list(map(int, input().split()))[::-1]
high = 10 ** 10 * 3
low = 0
while high - low > 1:
    mid = (high + low) // 2
    if can(mid, s1, s):
        high = mid
    else:
        low = mid
if can(low, s1, s):
    print(low)
else:
    print(high)
