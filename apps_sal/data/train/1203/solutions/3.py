mm = 1000000007


def pow1(a, b, MOD):
    x = 1
    y = a
    while(b > 0):
        if(b % 2 == 1):
            x = (x * y)
            if(x > MOD):
                x %= MOD
        y = (y * y)
        if(y > MOD):
            y %= MOD
        b = b / 2
    return x


def abc(a, b):
    c = 1
    d = 1
    b = min(b, a - b)
    for i in range(b):
        c = (c * a)
        c = c / (i + 1)
        a -= 1
        # d=(d*(i+1))
    # return (c*pow1(d,mm-2,mm))%mm
    return c % mm


p2 = [1, 2]
for i in range(2, 4001):
    p2.append((p2[-1] * 2) % mm)

t = int(input())
while t > 0:
    n, m = [int(x) for x in input().split()]
    while m > 0:
        a, b = [int(x) for x in input().split()]
        if b > a:
            print(0)
        else:
            r = abc(a - 1, b - 1)
            print((r * p2[n - a]) % mm)
        m -= 1
    t -= 1
