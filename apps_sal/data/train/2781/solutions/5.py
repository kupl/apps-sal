def longest_collatz(lst):
    return max(lst, key=seq_len)


def seq_len(n):
    count = 0
    while n > 1:
        n = 3 * n + 1 if n % 2 else n // 2
        count += 1
    return count
