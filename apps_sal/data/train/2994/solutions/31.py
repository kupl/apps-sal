def find_digit(num, nth):
    if nth > 0:
        try:
            return int(list(str(num)[::-1])[nth-1])
        except IndexError:
            return 0
    else:
        return -1
