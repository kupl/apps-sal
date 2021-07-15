from math import sqrt
for i in range(int(input())):
    a, b = list(map(int, input().split()))
    if not a < b:
        a, b = b, a
    ans = (a-1)*2 + (a < b-1)
    c = int(sqrt(a*b))
    if c**2 == a*b:
        c -= 1
    if a < c:
        if (a*b) % c == 0:
            d = (a*b)//c - 1
        else:
            d = a*b//c
        ans += (c - a) * 2 - (c==d)
    print(ans)



