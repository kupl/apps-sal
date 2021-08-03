def find_digit(num, nth):
    try:
        if nth > 0:
            return int(str(num)[-nth])
        return -1
    except:
        return 0
