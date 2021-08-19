import math


def no(n):
    c = 0
    while n > 0:
        c += 1
        n //= 10
    return c


# Function to find modulo inverse of b. It returns
# -1 when inverse doesn't
# modInverse works for prime m
def modInverse(a, m):
    m0 = m
    y = 0
    x = 1

    if (m == 1):
        return 0

    while (a > 1):

        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if (x < 0):
        x = x + m0

    return x


# Function to compute a/b under modulo m


for _ in range(int(input())):
    a, n, m = map(int, input().split(' '))
    s = no(a)
    c = 10**s - 1
    if math.gcd(c, m) == 1:
        b = pow(10, n * s, m) - 1
        r = modInverse(c, m)
        d = (b % m) * (r % m)
    else:
        w = c * m
        b = pow(10, n * s, w) - 1
        d = b // c
    ans = (d % m) * (a % m)
    print(ans % m)
