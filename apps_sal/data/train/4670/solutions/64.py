def string_to_number(s):
    value = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    result = 0
    pos_or_neg = 1
    for i in s:
        if i == '-':
            pos_or_neg = -1
        if i in value:
            result = result * 10 + value[i]
    return result * pos_or_neg
