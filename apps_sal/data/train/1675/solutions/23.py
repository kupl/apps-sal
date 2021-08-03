def __starting_point():
    TC = int(input())
    for _ in range(TC):
        line = input()
        N = int(input())
        arr = []
        for _ in range(N):
            x, y = list(map(int, input().strip().split()))
            arr.append((x, y))
        arr.sort(key=lambda a: (a[0], a[1] * -1))
        dist = 0
        for i in range(1, N):
            x1 = arr[i][0]
            y1 = arr[i][1]
            x2 = arr[i - 1][0]
            y2 = arr[i - 1][1]
            d = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
            dist += d

        print("{:0.2f}".format(dist))


__starting_point()
