def difference_in_ages(ages):
    ages.sort()
    result = []
    res1 = ages[-1] - ages[0]
    res2 = ages[0]
    res3 = ages[-1]

    return res2, res3, res1

