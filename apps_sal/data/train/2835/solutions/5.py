def isPrime(n):
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def solve(a, b):
    s = '2'
    i = 3
    while len(s) < (a + b):
        if isPrime(i):
            s += str(i)
        i += 2
    return s[a:a + b]
