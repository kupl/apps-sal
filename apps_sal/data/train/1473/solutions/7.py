try:
    t = eval(input())
except EOFError:
    t = 0
while t:
    try:
        (r, c, m, k, j) = list(map(int, input().split()))
    except EOFError:
        r = 1
        c = 1
        m = 1
        k = 1
        j = 1
    area1 = r * c
    area2 = m + k + j
    if area1 != area2:
        print('No')
    else:
        f = 0
        if m % r == 0:
            rr = r
            cc = c
            a = m // rr
            cc = cc - a
            if k % rr == 0 and j % rr == 0 or (k % cc == 0 and j % cc == 0):
                f = 1
        if m % c == 0 and f == 0:
            rr = r
            cc = c
            a = m // cc
            rr -= a
            if k % rr == 0 and j % rr == 0 or (k % cc == 0 and j % cc == 0):
                f = 1
        if k % r == 0 and f == 0:
            rr = r
            cc = c
            a = k // rr
            cc = cc - a
            if m % rr == 0 and j % rr == 0 or (m % cc == 0 and j % cc == 0):
                f = 1
        if k % c == 0 and f == 0:
            rr = r
            cc = c
            a = k // cc
            rr = rr - a
            if m % rr == 0 and j % rr == 0 or (m % cc == 0 and j % cc == 0):
                f = 1
        if j % r == 0 and f == 0:
            rr = r
            cc = c
            a = j // rr
            cc = cc - a
            if k % rr == 0 and m % rr == 0 or (k % cc == 0 and m % cc == 0):
                f = 1
        if j % c == 0 and f == 0:
            rr = r
            cc = c
            a = j // cc
            rr = rr - a
            if k % rr == 0 and m % rr == 0 or (k % cc == 0 and m % cc == 0):
                f = 1
        if f == 1:
            print('Yes')
        else:
            print('No')
    t = t - 1
