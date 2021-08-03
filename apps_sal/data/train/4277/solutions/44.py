def difference_in_ages(ages):
    a = max(ages)
    b = min(ages)
    dif = abs(a - b)
    return (b, a, dif)
