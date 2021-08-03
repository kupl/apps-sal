t = int(input())
while t > 0:
    t = t - 1
    n = int(input())

    l = list(map(int, input().split()))
    l.sort()
    max1 = 0
    for i in range(len(l)):
        if i == 0:
            dist = abs(l[i + 1] - l[i])
            max1 = max(dist, max1)
        elif i == len(l) - 1:
            dist = abs(l[i] - l[i - 1])
            max1 = max(dist, max1)
        else:
            dist = min(abs(l[i + 1] - l[i]), abs(l[i] - l[i - 1]))
            max1 = max(dist, max1)
    print(max1)
