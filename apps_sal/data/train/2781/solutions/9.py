def longest_collatz(input_array):
    def collatz_len(n):
        ctr = 0
        while n > 1:
            ctr, n = ctr + 1, (n // 2 if n % 2 == 0 else 3 * n + 1)
        return ctr
    return max((n for n in input_array), key=collatz_len)
