def isprime(n):
    if n <= 1:
        return 0
    if n <= 3:
        return 1
    if not n % 2 or not n % 3:
        return 0
    for i in range(5, int(pow(n, 0.5)) + 1, 2):
        if not n % i:
            return 0
    return 1


def abc(n, k):
    if n == 0:
        if k % 2:
            return True
        return False
    if k % 2:
        x = abc(n - 1, k + 1)
        for j in range(3, n + 1, 2):
            if not n % j:
                x = x or abc(n // j, k + 1)
        return x
    x = abc(n - 1, k + 1)
    for j in range(3, n + 1, 2):
        if not n % j:
            x = x and abc(n // j, k + 1)
    return x


t = int(input())
for _ in range(t):
    n = int(input())
    if n & n - 1 == 0:
        if n == 2:
            print('Me')
        else:
            print('Grinch')
    elif not n % 2:
        n = n // 2
        if isprime(n):
            print('Grinch')
        else:
            print('Me')
    else:
        print('Me')
