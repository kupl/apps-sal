def expmod(a, n, m):
    if n == 0:
        return 1
    elif n == 1:
        return a%m
    res = n/2
    rem = n%2
    temp = expmod(a, res, m)
    if rem == 1:
        return temp*temp*a % m
    else:
        return temp*temp % m

n, p, k = list(map(int, input().split()))


a= list(map(int, input().split()))
holes = {}
res = 0
for i in range(0, n):
    temp = ((expmod(a[i], 4, p) - k*a[i])%p + p)%p
    if temp in holes:
        res+=holes[temp]
        holes[temp]+=1
    else:
        holes[temp]=1

print(int(res))

