def all_non_consecutive(lst):
    return [{'i': i, 'n': n} for (i, n) in enumerate(lst[1:], 1) if n != lst[i - 1] + 1]
