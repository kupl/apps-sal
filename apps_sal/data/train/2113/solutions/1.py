from sys import *

n = int(stdin.readline().strip())
s1 = stdin.readline().strip()
a = list(map(int, s1.split()))

if n == 1:
    print('0')
else:
    x = 0
    n0 = 1
    while n0 < n:
        n0 = n0 * 2
    b = [0] * (2 * n0 + 10)
    '''for i in range (n-1):
        for j in range (i+1,n):
            if a[i]>a[j]:
                x+=1'''
    for i in range(n):
        t = a[i]
        u = 0
        k = 1
        j = 1
        while t > 0:
            if (t >> j) << j != t:
                u = u + b[(n0 + t - 1) >> (j - 1)]
                t = t - k
            k = k << 1
            j = j + 1
        x = x + u
        j = n0 + a[i] - 1
        while j > 0:
            b[j] += 1
            j = j >> 1

    x = ((n * (n - 1)) // 2) - x
    '''n=x//2
    print(x,n,' !!!')
    r=x
    i=1
    bi=n
    eps=0.0000001
    if x>0:
        while (x+2*i)*bi*((0.5)**i)>eps:
            r=r+(x+2*i)*bi*((0.5)**i)
            bi=(bi*(n+i))//(i+1)
            i=i+1
    else:
        r=0
    r=r*((0.5)**n)
    print("%.7f"%r)'''
    if x % 2 == 1:
        print(2 * x - 1)
    else:
        print(2 * x)
