def square_free_part(n):

    def fac(n):
        return [i for i in range(2, n // 2 + 1) if n % i == 0] + [n]

    def issquare(n):
        return True if str(n ** 0.5)[-1] == '0' else False
    if isinstance(n, bool):
        return None
    if isinstance(n, int) and n > 0:
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in sorted(fac(n), reverse=True):
            if sum([issquare(f) for f in fac(i)]) == 0:
                return i
    else:
        return None
