def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


def solve(n):
    if isPrime(n):
        return n
    add = 1
    rem = 1
    ans = None
    while True:
        if isPrime(n + add):
            ans = n + add
        if isPrime(n - rem):
            ans = n - rem
        if ans != None:
            return ans
        add += 1
        rem += 1
