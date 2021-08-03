t = int(input())
for _ in range(t):
    n = int(input())
    ar = []
    y = []
    for i in range(n):
        ar.append(list(map(int, input().split())))
        y.append(ar[-1][1])
        ar[-1].append(i)

    y.sort()
    mny = y[0]
    mxy = y[-1]
    ar.sort()
    ssx, ssy, ssi = ar[0]
    bbx, bby, bbi = ar[-1]

    sbx, sby, sbi = ar[0]
    bsx, bsy, bsi = ar[-1]

    for i in range(len(ar)):
        if ar[i][0] > ssx:
            sbx, sby, sbi = ar[i - 1]
            break

    for i in range(len(ar) - 1, -1, -1):
        if ar[i][0] < bsx:
            bsx, bsy, bsi = ar[i + 1]
            break

    if (ssy <= mny):
        print(1)
        print(ssi + 1, 'NE')
        continue
    if (sby >= mxy):
        print(1)
        print(sbi + 1, 'SE')
        continue
    if (bsy <= mny):
        print(1)
        print(bsi + 1, 'NW')
        continue
    if (bby >= mxy):
        print(1)
        print(bbi + 1, 'SW')
        continue

    print(2)
    if(ssy < bby):
        print(ssi + 1, 'NE')
        print(bbi + 1, 'SW')
    else:
        print(ssi + 1, 'SE')
        print(bbi + 1, 'NW')
