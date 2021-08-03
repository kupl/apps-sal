T = int(input())

MAX = 33000

bePrime = [0] * MAX
primNum = []

for j in range(2, MAX):
    if bePrime[j] == 0:
        primNum.append(j)
        i = j
        while i < MAX:
            bePrime[i] = 1
            i = i + j


def isPrime(a):
    for j in primNum:
        if j >= a:
            return True
        if a % j == 0:
            return False
    return True


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


while T > 0:
    num = 0
    n = int(input())

    m = n
    while isPrime(m) == False:
        m -= 1
    while isPrime(n + 1) == False:
        n += 1
        num += 1

    a = n - 1
    b = 2 * (n + 1)

    a = a * (n + 1) * m - num * b
    b = b * (n + 1) * m

    g = gcd(a, b)
    a //= g
    b //= g

    print('{0}/{1}'.format(a, b))
    T -= 1
