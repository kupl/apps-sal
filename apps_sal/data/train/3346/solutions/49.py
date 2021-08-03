def IsPrime(n):
    i = 2
    limit = int(n**0.5)
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True


def gap(g, m, n):
    a = []
    while m < n:
        k = m + 1
        if IsPrime(m) and IsPrime(m + g):
            while k < m + g:
                if IsPrime(k):
                    m += 1
                    break
                else:
                    k += 1
            if IsPrime(m) and IsPrime(m + g):
                return [m, m + g]
        m += 1
    return None
