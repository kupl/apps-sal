def difference_in_ages(ages):
    min = ages[0]
    max = ages[0]
    for age in ages:
        if age < min:
            min = age
        if age > max:
            max = age
    diff = max - min
    return (min, max, diff)
