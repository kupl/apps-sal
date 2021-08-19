def valid(coolTime):
    Time = c[0]
    for i in range(1, n):
        if Time + coolTime < c[i]:
            Time = c[i]
        elif Time + coolTime <= c[i] + d:
            Time = Time + coolTime
        else:
            return False
    return True


e = 1e-06
test = int(input())
for _ in range(test):
    l = input().split()
    n = int(l[0])
    d = int(l[1])
    c = list(map(int, input().split()))
    c.sort()
    low = 0.0
    high = 4000000000.0
    while high - low > e:
        mid = (low + high) / 2.0
        if valid(mid):
            low = mid
        else:
            high = mid
    print(mid)
