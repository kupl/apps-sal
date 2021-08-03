def difference_in_ages(ages):
    ages.sort()
    a = ages[-1]
    b = ages[0]
    c = a - b
    return (b, a, c)
