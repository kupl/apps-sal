from collections import defaultdict, Counter

# the special case allows for linear solution


def exchange_sort(sequence):
    n_sevens, n_eights = sequence.count(7), sequence.count(8)
    sevens = defaultdict(lambda: 0, Counter(sequence[:n_sevens]))
    eights = defaultdict(lambda: 0, Counter(sequence[n_sevens:n_sevens + n_eights]))
    nines = defaultdict(lambda: 0, Counter(sequence[n_sevens + n_eights:]))
    direct_78 = min(sevens[8], eights[7])
    direct_79 = min(sevens[9], nines[7])
    direct_89 = min(eights[9], nines[8])
    sevens[8] -= direct_78
    nines[7] -= direct_79
    nines[8] -= direct_89
    eights[7] -= direct_78
    eights[9] -= direct_89
    sevens[7], eights[8], nines[9] = 0, 0, 0
    return direct_78 + direct_79 + direct_89 + sum(nines.values()) * 2
