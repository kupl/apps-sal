from collections import Counter

def exchange_sort(sequence):
    a, b, c = map(Counter(sequence).get, (7, 8, 9))
    if not (a and b and c): return sum(x < y for x,y in zip(sorted(sequence), sequence))
    return sequence[a:].count(7) + max(sequence[-c:].count(8), sequence[a:-c].count(9))
