def mormons(number, reach, target):
    c = 0
    while number < target:
        number += reach * number
        c += 1
    return c
