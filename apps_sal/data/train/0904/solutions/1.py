# cook your dish here
import bisect
for _ in range(int(input())):

    n, x = list(map(int, input().split()))

    l = list(map(int, input().split()))
    battery = []

    power = 0
    i = 0
    t = (n + 1) // 2
    while power < x and i < t:

        if i == n - i - 1:
            temp = [-1, l[i]]
        else:
            temp = sorted([l[i], l[n - i - 1]])

        power += temp[1]
        pos = bisect.bisect_right(battery, temp[1], lo=0, hi=len(battery))
        battery.insert(pos, temp[1])

        if temp[0] > battery[0]:

            power -= battery.pop(0)
            power += temp[0]
            pos = bisect.bisect_right(battery, temp[0], lo=0, hi=len(battery))
            battery.insert(pos, temp[0])

        i += 1

    if power >= x:
        print('YES')
    else:
        print('NO')
