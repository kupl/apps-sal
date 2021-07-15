def difference_in_ages(ages):
    ages.sort()
    lst = []
    lst.append(ages[0])
    lst.append(ages[-1])
    lst.append(ages[-1]-ages[0])
    m = tuple(lst)
    return m
