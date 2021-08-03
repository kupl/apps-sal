t = int(input())

for x in range(t):

    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    tarr = []
    marr = []
    for i in range(n):
        if((i + 1) % 2 == 0):
            tarr.append(a[i])
        else:
            marr.append(a[i])

    tarr.sort()
    marr.sort(reverse=True)

    for i in range(k):
        if(sum(tarr) > sum(marr) or (i == len(tarr) or i == len(marr))):
            break
        tarr[i], marr[i] = marr[i], tarr[i]

    #print(tarr, marr)

    t = sum(tarr)
    m = sum(marr)

    if(t > m):
        print('YES')
    else:
        print('NO')
