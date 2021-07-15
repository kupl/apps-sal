from collections import Counter

def odd_ones_out(numbers):
    c = Counter(numbers)
    return [n for n in numbers if c[n] % 2 == 0]
