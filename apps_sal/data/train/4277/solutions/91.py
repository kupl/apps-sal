def difference_in_ages(ages):
    ages.sort()
    youngest = ages[0]
    oldest = ages[-1]
    diff = oldest - youngest
    return (youngest, oldest, diff)
