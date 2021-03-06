def isValid(mid):
    time = 0.0
    for i in range(n):
        if time < c[i]:
            time = c[i]
            time += mid
        elif time >= c[i] and time <= c[i] + d:
            time += mid
        else:
            return False
    return True


t = int(input())
while t != 0:
    (n, d) = list(map(int, input().split()))
    c = list(map(int, input().split()))[:n]
    ans = -1
    c.sort()
    (low, high) = (0, 10 ** 10)
    while high - low > 1e-06:
        mid = (low + high) / 2
        if isValid(mid):
            ans = mid
            low = mid
        else:
            high = mid
    print('{0:.6f}'.format(ans))
    t -= 1
