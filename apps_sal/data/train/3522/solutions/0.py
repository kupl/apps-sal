def max_gap(numbers):
    lst = sorted(numbers)
    return max((b - a for (a, b) in zip(lst, lst[1:])))
