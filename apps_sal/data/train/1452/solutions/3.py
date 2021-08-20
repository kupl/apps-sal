import fractions


def eval(n, m):
    g = fractions.gcd(n, m)
    if g == n:
        if n == 1:
            print('Yes')
        else:
            print('No 1')
    elif g == 1:
        print('Yes')
    else:
        print('No %d' % (n / g))


t = int(input())
for _ in range(t):
    (n, m) = [int(x) for x in input().split()]
    eval(n, m)
