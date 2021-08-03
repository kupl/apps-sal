def find_digit(num, nth):
    if nth < 1:
        return -1

    num = str(abs(num))
    if nth > len(num):
        return 0
    calc = len(num) - nth
    return int(num[calc])
