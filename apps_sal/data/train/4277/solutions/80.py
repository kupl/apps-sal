def difference_in_ages(ages):
    smallest = ages[0]
    largest = ages[1]
    for age in ages:
        if smallest > age:
            smallest = age
        if largest < age:
            largest = age
    return (smallest, largest, largest - smallest)
