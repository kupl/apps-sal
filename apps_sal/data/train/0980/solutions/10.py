t = int(input())
while(t > 0):
    ans = 0
    t -= 1
    s = input()
    n, b, m = s.split()
    n = int(n)
    b = int(b)
    m = int(m)
    n1 = n
    while(n > 0):
        if n % 2 == 0:
            half = n / 2
        else:
            half = (n + 1) / 2
        ans += half * m
        n -= half
        m *= 2
        if n > 0:
            ans += b
    print(ans)
