def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)


t = int(input())
while t:
    par = [int(i) for i in input().split(' ')]
    (n, m) = (par[0], par[1])
    g_div = gcd(n, m)
    if g_div == 1:
        print('Yes')
    else:
        print('No ' + str(int(n / g_div)))
    t = t - 1
