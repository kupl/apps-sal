def difference_in_ages(ages):
    ages.sort()
    agelen = len(ages)
    return(ages[0], ages[agelen -1],(ages[agelen-1] - ages[0]))
