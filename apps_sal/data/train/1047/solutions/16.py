t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    mp, mn = [], []
    for i in range(n):
        x, y = list(map(int, input().split()))
        mp.append(y - x)
        mn.append(y + x)
    dmin = abs(mp[1] - mp[0])
    mp.sort()
    mn.sort()
    for i in range(n - 1):
        dmin = min(dmin, mp[i + 1] - mp[i])
        dmin = min(dmin, mn[i + 1] - mn[i])
    if dmin % 2 == 0:
        print(dmin // 2)
    else:
        print(dmin / 2)
