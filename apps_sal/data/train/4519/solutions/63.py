def max_number(number):
    return int(''.join((x for x in sorted([i for i in str(number)])))[::-1])
