from collections import Counter


def odd_ones_out(numbers):
    cnt = Counter(numbers)
    return [v for v in numbers if not cnt[v] & 1]
