def difference_in_ages(ages):
    young = 10000000
    old = 0
    for x in ages:
        if x < young:
            young = x
        if x > old:
            old = x
    difference = old - young
    ris = (young, old, difference)
    return ris
