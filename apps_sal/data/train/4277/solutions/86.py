def difference_in_ages(ages):
    ages.sort()
    diference = []
    diference.append(ages[0])
    diference.append(ages[len(ages) - 1])
    diference.append(ages[len(ages) - 1] - ages[0])
    return tuple(diference)
