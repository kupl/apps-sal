import math


def round_it(n):
    number_as_string = str(n)
    size_of_number = len(number_as_string) - 1
    index_of_decimal = number_as_string.index('.')

    if (size_of_number / 2 == index_of_decimal):
        return round(n)
    elif (size_of_number / 2 > index_of_decimal):
        return math.ceil(n)
    else:
        return math.floor(n)
