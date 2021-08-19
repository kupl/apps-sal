cache = {1: 1}


def max_collatz_length(n):

    def collatz(n):
        if n in cache:
            return cache[n]
        next_n = 3 * n + 1 if n % 2 else n / 2
        ret = cache[n] = 1 + collatz(next_n)
        return ret
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        return []
    return max(([i, collatz(i)] for i in range(1, n + 1)), key=lambda p: p[1])
