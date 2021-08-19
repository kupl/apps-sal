def gap(g, m, n):

    def isprime(a):
        a = abs(int(a))
        if a < 2:
            return False
        if a == 2:
            return True
        if not a & 1:
            return False
        for x in range(3, int(a ** 0.5) + 1, 2):
            if a % x == 0:
                return False
        return True
    if g & 1:
        if 2 >= m and 2 <= n:
            if isprime(2 + g):
                return [2, 2 + g]
    else:
        begin = m + (not m & 1)
        status = False
        result = []
        for j in range(begin, n, g):
            for i in range(int(g / 2)):
                if isprime(j + 2 * i):
                    if status:
                        status = False
                        break
                    if isprime(j + 2 * i + g):
                        result = [j + 2 * i, j + 2 * i + g]
                        status = True
                elif isprime(j + 2 * i + g):
                    if not status:
                        break
            if status:
                return result
    return None
