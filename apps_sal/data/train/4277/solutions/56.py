def difference_in_ages(ages):
    result = [min(ages), max(ages), (max(ages) - min(ages))]
    return tuple(result)
