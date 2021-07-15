def difference_in_ages(ages):
    ages.sort()
    poo = (ages[0],ages[-1],ages[-1] - ages[0])
    return poo
