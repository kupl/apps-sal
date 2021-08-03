def difference_in_ages(ages):
    x = sorted(ages)
    return (x[0], x[len(ages) - 1], x[len(ages) - 1] - x[0])
