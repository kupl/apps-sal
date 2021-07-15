def difference_in_ages(ages):
    ages = sorted(ages)
    ages_diff = (ages[0],ages[-1],ages[-1] - ages[0])
    return ages_diff
