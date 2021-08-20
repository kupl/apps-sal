def max_sum(lst, ranges):
    return max((sum(lst[i:j + 1]) for (i, j) in ranges))
