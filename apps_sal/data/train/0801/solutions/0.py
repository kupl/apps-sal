from collections import Counter
tc = int(input())
for k in range(tc):
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    cc = sorted(a + b)
    p = []
    q = []
    for i in range(0, 2 * n, 2):
        p.append(cc[i])
    for i in range(1, 2 * n + 1, 2):
        q.append(cc[i])
    if p != q:
        print('-1')
        continue
    a.sort()
    b.sort()
    if a == b:
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
        if gb[i] <= zz * 2:
            ans += gb[i]
        else:
            ans += zz * 2
    print(ans)
'c = []\ni, j = 0, 0\nwhile i < len(a) and j < len(b):\n    if a[i] == b[j]:\n     c.append(a[i])\n     i += 1\n     j += 1\n    elif a[i] > b[j]:\n     j += 1\n    else:\n     i += 1'
