def gap(g, m, n):

    def is_prime(p):
        if p % 2 == 0:
            return False
        for i in range(3, int(p ** 0.5) + 1, 2):
            if p % i == 0:
                return False
        return True
    first = 0
    for t in range(m, n + 1):
        if not is_prime(t):
            continue
        if first == 0:
            first = t
        elif t - first == g:
            return [first, t]
        else:
            first = t
    return None
