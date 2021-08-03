from math import log10

seq = {0: 1, 1: 1, 2: 2, 3: 2, 4: 3, 5: 3}
len_seq = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1}


def next_term(n): return seq[n - 1] * seq[n - 2] * seq[n - 3] - seq[n - 4] * seq[n - 5] * seq[n - 6]
def count_digits(n): return int(log10(n)) + 1


def something_acci(num_digits):
    i = 0
    while True:
        if i not in seq:
            n = next_term(i)
            seq[i], len_seq[i] = n, count_digits(n)
        if len_seq[i] >= num_digits:
            return i + 1, len_seq[i]
        i += 1
