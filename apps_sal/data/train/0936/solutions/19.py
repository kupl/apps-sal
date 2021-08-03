t = int(input())
while t > 0:
    count = 0
    n = int(input())
    l = []
    for i in range(n):
        l.append([int(x) for x in input().split()])
    for x in range(n - 1, 0, -1):
        r = l[x][x - 1] + 1
        if r != l[x][x]:
            count += 1
            k = x + 1
            for i in range(k):
                for j in range(i, k):
                    temp = l[i][j]
                    l[i][j] = l[j][i]
                    l[j][i] = temp
    t -= 1
    print(count)
