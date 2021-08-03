import numpy as np

t = int(input())
while(t):
    t -= 1
    n, m = list(map(int, input().split()))
    '''
    a=range(1,n+1)
    if m!=0:
     a=a[m:]+a[:m]
    '''
    b = np.zeros(n, dtype='bool')

    # print b
    pos = 0
    while(True):
        if b[(pos + m) % n] == True:
            break
        else:
            b[(pos + m) % n] = True
            pos = (pos + m) % n

        # print b,pos

    s = sum(b)
    if s == n:
        print('Yes')
    else:
        print('No' + ' ' + str(s))
