def count_inversions(lst):
    return sum(1 for i, m in enumerate(lst, 1) for n in lst[i:] if n < m)

