import numpy as np
t = int(input())
while t:
    t -= 1
    (n, m) = list(map(int, input().split()))
    '\n    a=range(1,n+1)\n    if m!=0:\n     a=a[m:]+a[:m]\n    '
    b = np.zeros(n, dtype='bool')
    pos = 0
    while True:
        if b[(pos + m) % n] == True:
            break
        else:
            b[(pos + m) % n] = True
            pos = (pos + m) % n
    s = sum(b)
    if s == n:
        print('Yes')
    else:
        print('No' + ' ' + str(s))
