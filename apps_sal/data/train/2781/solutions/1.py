def collatz(n, t=1):
    return t if n == 1 else collatz(n / 2 if n % 2 == 0 else 3 * n + 1, t + 1)


def longest_collatz(input_array):
    return sorted(list(zip(list(map(collatz, input_array)), input_array)))[-1][1]
