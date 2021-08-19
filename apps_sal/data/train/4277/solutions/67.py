def difference_in_ages(ages):
    ages.sort()
    summary = (ages[0], ages[-1], ages[-1] - ages[0])
    return summary
