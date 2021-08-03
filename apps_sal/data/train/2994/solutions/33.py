def find_digit(num, nth):
    if nth > len(str(num).replace('-', '')) and nth > 0:
        return 0
    elif nth <= 0:
        return -1
    else:
        return int(str(num).replace('-', '')[-nth])
