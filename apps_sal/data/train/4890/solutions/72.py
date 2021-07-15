def find_difference(a, b):
    accumulator1 = 1
    accumulator2 = 1
    for eachvalue in a:
        accumulator1 = accumulator1 * eachvalue
    for eachvalue in b:
        accumulator2 = accumulator2 * eachvalue
    return abs(accumulator1 - accumulator2)
