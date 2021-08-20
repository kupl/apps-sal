def alternate_sq_sum(a):
    return sum((a[i] ** 2 if i % 2 else a[i] for i in range(len(a)))) or 0
