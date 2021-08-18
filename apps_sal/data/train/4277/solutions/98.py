def difference_in_ages(ages):
    ages.sort()
    young = ages[0]
    old = ages[len(ages) - 1]
    return (young, old, old - young)
