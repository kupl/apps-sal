def difference_in_ages(ages):
    ages.sort()
    oldest_age = ages[-1]
    youngest_age = ages[0]
    diff = ages[-1] - ages[0]
    return tuple([youngest_age,oldest_age,diff])

