def difference_in_ages(ages):
    ages.sort()
    min_age = ages[0]
    max_age = ages[-1]
    return (min_age, max_age, max_age - min_age)
