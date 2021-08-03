
def difference_in_ages(ages):
    a = ages[0]
    b = ages[0]
    for i in ages:
        if i < a:
            a = i
    for x in ages:
        if b <= x:
            b = x
    return a, b, b - a
