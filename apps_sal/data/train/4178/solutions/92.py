def min_sum(a):
    return sum((x * y for (x, y) in zip(list(sorted(a)[:len(a) // 2]), list(sorted(a, reverse=True)[:len(a) // 2]))))
