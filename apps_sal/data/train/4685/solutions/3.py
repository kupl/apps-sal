from collections import Counter


def self_descriptive(num):
    s = str(num)
    return Counter(s) == {str(i): int(n) for i, n in enumerate(s) if n != '0'}
