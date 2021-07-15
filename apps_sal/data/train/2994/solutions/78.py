def find_digit(num, nth):
    if nth <= 0:
        return -1
    elif len(str(num)) < nth:
        return 0
    else:
        num = abs(num)
        num = [int(d) for d in str(num)]
        return num[-nth]

