def hotpo(n):

    def __collatz(n):
        return n / 2 if n % 2 == 0 else 3 * n + 1
    count = 0
    while True:
        if n == 1:
            return count
        n = __collatz(n)
        count += 1
