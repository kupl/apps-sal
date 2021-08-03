n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
l = sum(a)
if(l % k != 0):
    print('No')
    return
else:
    z = l // k
    c = []
    h = 0
    q = 0
    for i in range(len(a)):
        q += a[i]
        if(q == z):
            c.append(i + 1)
            q = 0
    c.reverse()
    for i in range(len(c) - 1):
        c[i] -= c[i + 1]
    c.reverse()
    if(len(c) == k):
        print('Yes')
        print(*c)
    else:
        print('No')
