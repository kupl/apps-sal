def lamps(lst):
    starts_with_zero = sum((on ^ i & 1 for (i, on) in enumerate(lst)))
    starts_with_one = sum((on ^ i & 1 for (i, on) in enumerate(lst, 1)))
    return min(starts_with_zero, starts_with_one)
