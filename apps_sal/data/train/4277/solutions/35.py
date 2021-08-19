def difference_in_ages(ages):
    l = min(ages)
    p = max(ages)
    s = min(ages) - max(ages)
    return (l, p, abs(s))
