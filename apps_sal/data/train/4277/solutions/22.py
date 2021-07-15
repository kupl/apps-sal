def difference_in_ages(ages):
    ages.sort()
    older = ages[-1]
    younger = ages[0]
    difference = older - younger
    return (younger, older, difference)
