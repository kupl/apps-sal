def longest_collatz(arr):
    return max([(gen_s(e), e) for e in arr])[1]


def gen_s(n, c=1):
    return c + gen_s((n // 2, n * 3 + 1)[n % 2], c + 1) if n != 1 else 1
