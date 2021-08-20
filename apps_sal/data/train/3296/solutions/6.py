SUFFIX_ONE = 'st'
SUFFIX_TWO = 'nd'
SUFFIX_THREE = 'rd'
SUFFIX_OTHER = 'th'


def what_century(year):
    century = 1 + (int(year) - 1) // 100
    return str(century) + ordinal_suffix(century)


def ordinal_suffix(number):
    if number // 10 == 1:
        return SUFFIX_OTHER
    elif number % 10 == 1:
        return SUFFIX_ONE
    elif number % 10 == 2:
        return SUFFIX_TWO
    elif number % 10 == 3:
        return SUFFIX_THREE
    else:
        return SUFFIX_OTHER
