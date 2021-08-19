import heapq
for _ in range(int(input())):
    (n, x) = list(map(int, input().split()))
    l = list(map(int, input().split()))
    battery = []
    heapq.heapify(battery)
    power = 0
    i = 0
    t = (n + 1) // 2
    while power < x and i < t:
        if i == n - i - 1:
            temp = [-1, l[i]]
        else:
            temp = sorted([l[i], l[n - i - 1]])
        power += temp[1]
        heapq.heappush(battery, temp[1])
        y = heapq.heappop(battery)
        heapq.heappush(battery, y)
        if temp[0] > y:
            power -= heapq.heappop(battery)
            power += temp[0]
            heapq.heappush(battery, temp[0])
        i += 1
    if power >= x:
        print('YES')
    else:
        print('NO')
