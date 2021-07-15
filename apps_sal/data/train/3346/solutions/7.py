def gap(g, m, n):
    import math
    simple = []
    numbers = []
    d = 3
    for i in range(m,n+1):
        if i%2==0:
            pass
        else:
            while d*d <=i and  i%d !=0:
                d+=2
            if d*d>i:
                simple.append(i)
                p = math.fabs(i - simple[simple.index(i) - 1])
                if p == g:
                    return [i-g,i]
            d = 3

    return None


