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


p = [x for x in range(1, 50001) if not is_prime(x) and all(d not in '2357' for d in str(x))]


def solve(n):
    return p[n]
