def difference_in_ages(ages):
    ages.sort()
    m = ages[0]
    u = ages[-1]
    return m, u, u - m
