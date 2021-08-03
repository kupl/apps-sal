def prime_test(n):
    # Miller-Rabin prime test
    d = n - 1
    r = 0
    while d % 2 != 0:
        d //= 2
        r += 1

    tests = [2, 3]
    if n > 100000:
        tests.append(5)

    for a in tests:
        if a >= n - 2:
            continue

        x = pow(a, d, n)
        if x == 1:
            continue

        flag = False
        for _ in range(r):
            if x == n - 1:
                flag = True
                break

            x = x**2 % n
        if flag:
            continue

        return False
    return True


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    return prime_test(n)


def gap(g, m, n):
    if g > n - m or (g % 2 == 1 and g > 1):
        return None

    p1, p2 = n, n

    for i in range(m, n + 1):
        if is_prime(i):
            p1, p2 = p2, i
            if p2 - p1 == g:
                return [p1, p2]

    return None
