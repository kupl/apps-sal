t = int(input())
while t:
    t = t - 1
    n = int(input())
    a = list(map(int, input().split()))
    fin = []
    fin.append(0)
    for i in range(n):
        if a[i] % 2 == 0:
            p = fin[-1]
            fin.append(p + 1)
        else:
            p = fin[-1]
            fin.append(p)
    que = int(input())
    while que > 0:
        que = que - 1
        (r, ti) = list(map(int, input().split()))
        m = fin[ti]
        n = fin[r - 1]
        even = m - n
        if even == 0:
            print('ODD')
        else:
            print('EVEN')
