def men_from_boys(arr):
    return [*dict.fromkeys(sorted(filter(lambda x: x % 2 == 0, arr)) \
        + sorted(filter(lambda x: x % 2, arr), reverse = True) ).keys()]
