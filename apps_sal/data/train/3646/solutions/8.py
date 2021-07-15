f=[1,0,1,2,9,44]
for i in range(6,10000):
    f.append(i*f[-1]+(-1)**i)


def c(x,y):
    if y>x: return 0
    if y>(x//2): y=x-y
    mul=1
    for i in range(1,y+1):
        mul = mul*(x-i+1) // i
    print(mul)
    return mul


def fixed_points_perms(n,k):
    
    return c(n,k) * f[n-k]
