def prime(n):
    for i in range(2, 1000):
        if i != n and n % i == 0:
            return False
    return True


def step(g, m, n):
    for num in range(m, n + 1):
        if prime(num) and prime(num + g) and num + g <= n:
            return [num, num + g]
    return None
