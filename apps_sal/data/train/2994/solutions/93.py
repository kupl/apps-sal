def find_digit(num,nth):
    if nth <= 0:
        return -1
    else:
        num = str(abs(num))
        if nth > len(num):
            return 0
        else:
            return int(num[-nth])
