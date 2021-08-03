def longest_collatz(lst):
    return max(lst, key=seq_len)


def seq_len(n):
    count = 0
    while n > 1:
        n = (3 * n + 1) if n % 2 else (n // 2)
        count += 1
    return count

# two-liner
#seq_len = lambda n: 0 if n == 1 else 1 + seq_len(3 * n + 1 if n % 2 else n // 2)
#longest_collatz = lambda lst: max(lst, key=seq_len)
