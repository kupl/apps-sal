def gcd(a, b):
    if(a == 0):
        return b
    else:
        return gcd(b % a, a)


def fgcd(a):
    r = a[0]
    for i in range(1, len(a)):
        r = gcd(a[i], r)
        if(r == 1):
            return 1
    return r


t = int(input())
while t:
    t -= 1
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    # mn = min(a)
    mn = fgcd(a)
    # print(mn)
    c = 0
    if(n >= mn):
        c = n - mn
        print(c)
        continue
    while(n > 1):
        if(mn % n != 0):
            c += 1
            n -= 1
        else:
            break
    print(c)
