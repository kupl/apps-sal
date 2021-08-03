def difference_in_ages(ages):
    max = 0
    for i in ages:
        if i > max:
            max = i
    min = max
    for j in ages:
        if j < min:
            min = j
    a = max - min
    return (min, max, a)
