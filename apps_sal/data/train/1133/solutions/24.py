def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = a[0]
    for i in a[1:]:
        res = gcd(res, i)
    tot = 0
    for i in a:
        tot += i // res
    print(res, tot)
