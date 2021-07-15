def howmuch(m, n):
    val = []
    if m > n:
        m,n = n,m
        
    for i in range(m,n+1):
        if (i-2)%7 == 0 and (i-1)%9 == 0:
            val.append(['M: {}'.format(i), 'B: {}'.format(int((i-2)/7)), 'C: {}'.format(int((i-1)/9))])
    return val
