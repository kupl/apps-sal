def gap(g, m, n):
    prime_prev = n
    for i in range(m, n + 1):
        if prime_yn(i):
            if i - prime_prev == g:
                return [prime_prev, i]
            prime_prev = i
    return None


def prime_yn(x):
    for j in range(2, int(x**0.5 + 1)):
        if x % j == 0:
            return False
    return True
