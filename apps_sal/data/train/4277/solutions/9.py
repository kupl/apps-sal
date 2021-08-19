def difference_in_ages(ages):
    sortedages = sorted(ages)
    return (sortedages[0], sortedages[-1], sortedages[-1] - sortedages[0])
