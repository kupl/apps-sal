from collections import Counter


def histogram(values, bin_width):
    count = Counter(values)
    return [sum(count[i + x] for x in range(bin_width)) for i in range(0, max(count) + 1, bin_width)] if count else []
