def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    x = 3
    while(x * x <= n):
        if n % x == 0:
            return False
        x += 2
    return True


def make_prime_stream(n):
    s = '2'
    x = 3
    while(len(s) < n):
        if is_prime(x):
            s += str(x)
        x += 2
    return s


prime_stream = make_prime_stream(21000)


def solve(a, b):
    return prime_stream[a:a + b]
