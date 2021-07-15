# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n, = map(int,input().split())
*a, = map(int,input().split())
*b, = map(int,input().split())

def bsort(a,d):
    a0 = []
    a1 = []
    for i in a:
        if i>>d&1:
            a1.append(i)
        else:
            a0.append(i)
    return a0+a1
    

ans = 0
for d in range(29):
    res = 0
    a = bsort(a,d)
    b = bsort(b,d)
    r1 = r2 = r3 = 0
    MASK = (1<<(d+1))-1
    #print([i&MASK for i in a],[i&MASK for i in b])
    for bi in b[::-1]:
        bi &= MASK
        while r1 < n and bi+(a[r1]&MASK) < 1<<d:
            r1 += 1
        while r2 < n and bi+(a[r2]&MASK) < 2<<d:
            r2 += 1
        while r3 < n and bi+(a[r3]&MASK) < 3<<d:
            r3 += 1
        #print(d,bi,r1,r2,r3,n)
        res += r2-r1 + n-r3
    ans |= (res%2)<<d
    
print(ans)
