def isPrime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def prevPrime(n):
    while not isPrime(n):
        n -= 1
    return n


def nextPrime(n):
    n += 1
    while not isPrime(n):
        n += 1
    return n


def gcd(a, b):
    while a:
        b %= a
        (a, b) = (b, a)
    return b


def solve():
    n = int(input())
    prev = prevPrime(n)
    next = nextPrime(n)
    num1 = prev - 2
    den1 = prev * 2
    g = gcd(num1, den1)
    num1 //= g
    den1 //= g
    num2 = n - prev + 1
    den2 = prev * next
    g = gcd(num2, den2)
    num2 //= g
    den2 //= g
    g = gcd(num1 * den2 + num2 * den1, den1 * den2)
    x = (num1 * den2 + num2 * den1) // g
    y = den1 * den2 // g
    print('{}/{}'.format(x, y))


t = int(input())
while t:
    t -= 1
    solve()
