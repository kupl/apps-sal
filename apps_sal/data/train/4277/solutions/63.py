def difference_in_ages(ages):
    ages.sort()
    youngest = ages[0]
    oldest = ages[-1]
    difference = ages[-1] - ages[0]
    return youngest, oldest, difference
