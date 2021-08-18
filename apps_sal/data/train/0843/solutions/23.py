t = int(input())
while t:
    n = int(input())
    l = []
    for i in range(n):
        l1 = list(map(int, input().split()))
        l1 = sorted(l1)
        l.append(l1)
    count = l[n - 1][n - 1]
    m = l[n - 1][n - 1]
    c = 0
    k = 0
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, -1, -1):
            if(l[i][j] < m):
                count += l[i][j]
                m = l[i][j]
                c += 1
                break
        if(c == 0):
            print(-1)
            k += 1
            break
        else:
            c -= 1
    if(k == 0):
        print(count)
    t -= 1
