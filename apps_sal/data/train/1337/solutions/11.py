def lcm(a, b):
    if(a > b):
        num = a
        den = b
    else:
        num = b
        den = a
    rem = num % den
    while(rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    x = int(int(a * b) / int(gcd))
    return x


for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    r = int(input())
    if n == 1:
        print(p[0] + r)
    else:
        ans = lcm(p[0], p[1])
        for i in range(2, n):
            ans = lcm(ans, p[i])
        print(ans + r)
