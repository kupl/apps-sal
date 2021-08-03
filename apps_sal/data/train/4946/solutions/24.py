def house_numbers_sum(l):
    if not l[0]:
        return 0
    return l[0] + house_numbers_sum(l[1:])
