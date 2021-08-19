try:
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        x = int(input())
        a = list(map(int, input().split()))
        if 1 in a:
            print('Impossible')
        else:
            a.sort(reverse=True)
            (i, count, ct) = (len(a) - 1, 0, 0)
            v = 0
            while i >= 0:
                if a[i] - v == 1:
                    print('Impossible')
                    break
                ct += 1
                if ct == x:
                    ct = 0
                    count += 1
                    v += 1
                i -= 1
            print('Possible')
except:
    pass
