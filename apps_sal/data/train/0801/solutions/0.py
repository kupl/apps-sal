from collections import Counter
tc = int(input())
for k in range(tc):
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    cc = sorted(a + b)
    p = []
    q = []
    for i in range(0, (2 * n), 2):
        p.append(cc[i])
    for i in range(1, (2 * n) + 1, 2):
        q.append(cc[i])

    if(p != q):
        print('-1')
        continue
    a.sort()
    b.sort()
    if(a == b):
        print('0')
        continue
    xx = list((Counter(a) - Counter(p)).elements())
    yy = list((Counter(b) - Counter(p)).elements())
    iu = len(xx)
    gb = sorted(xx + yy)
    uu = xx[0]
    vv = yy[0]
    zz = min(cc[0], uu, vv)
    ans = 0
    for i in range(iu):
        if(gb[i] <= (zz * 2)):
            ans += gb[i]
        else:
            ans += (zz * 2)
    print(ans)


'''c = []
i, j = 0, 0
while i < len(a) and j < len(b):
    if a[i] == b[j]:
     c.append(a[i])
     i += 1
     j += 1
    elif a[i] > b[j]:
     j += 1
    else:
     i += 1'''
