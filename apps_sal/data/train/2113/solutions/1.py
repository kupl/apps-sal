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
    'for i in range (n-1):\n        for j in range (i+1,n):\n            if a[i]>a[j]:\n                x+=1'
    for i in range(n):
        t = a[i]
        u = 0
        k = 1
        j = 1
        while t > 0:
            if t >> j << j != t:
                u = u + b[n0 + t - 1 >> j - 1]
                t = t - k
            k = k << 1
            j = j + 1
        x = x + u
        j = n0 + a[i] - 1
        while j > 0:
            b[j] += 1
            j = j >> 1
    x = n * (n - 1) // 2 - x
    'n=x//2\n    print(x,n,\' !!!\')\n    r=x\n    i=1\n    bi=n\n    eps=0.0000001\n    if x>0:\n        while (x+2*i)*bi*((0.5)**i)>eps:\n            r=r+(x+2*i)*bi*((0.5)**i)\n            #print(r)\n            bi=(bi*(n+i))//(i+1)\n            i=i+1\n            #print(bi,i)\n    else:\n        r=0\n    r=r*((0.5)**n)\n    print("%.7f"%r)'
    if x % 2 == 1:
        print(2 * x - 1)
    else:
        print(2 * x)
