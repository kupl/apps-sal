def difference_in_ages(ages):
    x = sorted(ages)
    return (x[0], x[-1], x[-1] - x[0])
