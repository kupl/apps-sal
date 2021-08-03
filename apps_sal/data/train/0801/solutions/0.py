from collections import Counter
tc = int(input())
for k in range(tc):
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    cc = sorted(a + b)
    #print('cc = ',cc)
    p = []
    q = []
    #print('len(cc) = ',len(cc))
    #print('len = ',(2*n))
    # rx=0
    for i in range(0, (2 * n), 2):
        p.append(cc[i])
        # rx+=1
    for i in range(1, (2 * n) + 1, 2):
        q.append(cc[i])

    if(p != q):
        print('-1')
        continue
    a.sort()
    b.sort()
    # print(p)
    # print(q)
    if(a == b):
        print('0')
        continue
    xx = list((Counter(a) - Counter(p)).elements())
    yy = list((Counter(b) - Counter(p)).elements())
    #print('xx = ',xx)
    #print('yy = ',yy)
    iu = len(xx)
    gb = sorted(xx + yy)
    # print(iu)
    uu = xx[0]
    vv = yy[0]
    #print('uu = ',uu)
    #print('vv = ',vv)
    zz = min(cc[0], uu, vv)
    #print('zz = ',zz)
    ans = 0
    for i in range(iu):
        if(gb[i] <= (zz * 2)):
            ans += gb[i]
        else:
            ans += (zz * 2)
    print(ans)

#a = [1, 1, 1, 2, 3, 3]
#b = [1, 1, 2, 2, 3, 4]

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
# print(c)
