def difference_in_ages(ages):
    x = max(ages)
    y = min(ages)
    z = x - y
    return min(ages), max(ages), z
