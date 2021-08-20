from collections import Counter


def string_letter_count(s):
    counts = Counter(filter(str.islower, s.lower()))
    return ''.join((f'{n}{c}' for (c, n) in sorted(counts.items())))
