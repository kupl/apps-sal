t = int(input())
for cases in range(t):
    n = int(input())
    lis = []
    for i in range(n):
        lis1 = sorted(list(map(int, input().split())))
        lis.append(lis1)
    summ = lis[-1][-1]
    maxx = summ
    c = 1
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, -1, -1):
            if lis[i][j] < maxx:
                maxx = lis[i][j]
                c += 1
                summ += lis[i][j]
                break
    if c == n:
        print(summ)
    else:
        print(-1)
    print()
