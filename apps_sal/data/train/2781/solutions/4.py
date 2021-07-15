def longest_collatz(a):
    def f(n):
        r = 1
        while n > 1:
            n = n * 3 + 1 if n % 2 else n // 2
            r += 1
        return r
    return max(a, key=f)
