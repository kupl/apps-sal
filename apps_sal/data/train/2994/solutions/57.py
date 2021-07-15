def find_digit(num, nth):
    num = str(num)
    try:
        if nth <= 0 :
            return -1
        else:
            return int(num[-nth])
    except IndexError:
        return 0
