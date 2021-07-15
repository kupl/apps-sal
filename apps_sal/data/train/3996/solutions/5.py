def alternate_sq_sum(arr):
    return sum([x ** 2 if pos % 2 != 0 else x for pos, x in enumerate(arr)])
