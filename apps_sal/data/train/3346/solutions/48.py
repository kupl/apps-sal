def gap(g, m, n):

    def prime(p):
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:
                return False
        return True

    def gap_to_next_prime(p):
        q = p + 1
        while not prime(q):
            q += 1
        return q - p
    for p in range(m, n + 1 - g):
        if prime(p) and gap_to_next_prime(p) == g:
            return [p, p + g]
