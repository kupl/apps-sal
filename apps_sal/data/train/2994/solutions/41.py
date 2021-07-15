def find_digit(num, nth):
    if nth <= 0:
        return -1
    elif nth <= len(str(num)):
        num = str(num)
        number = num[-nth]
        return int(number)
    else:
        return 0
