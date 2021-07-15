def binary_cleaner(lst):
    return [n for n in lst if n < 2], [i for i, n in enumerate(lst) if n > 1]
