def isprime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


t = int(input())
while t > 0:
    n = int(input())
    x = n & -n
    if n == 2:
        print('Me')
    elif x == 2 and isprime(n // x) or n == 1 or x == n:
        print('Grinch')
    else:
        print('Me')
    t -= 1
