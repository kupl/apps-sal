def collatz(n):
    def f(n):
        while True:
            yield str(n)
            if n == 1:
                break
            elif n % 2:
                n = 3 * n + 1
            else:
                n //= 2
    return '->'.join(f(n))
