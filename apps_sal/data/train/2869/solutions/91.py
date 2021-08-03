from collections import Counter


def distinct(numbers):
    number_counts = Counter(numbers)

    return list(number_counts.keys())
