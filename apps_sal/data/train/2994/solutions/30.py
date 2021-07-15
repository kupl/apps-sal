def find_digit(num, nth):
    try:
        if nth>0:
            return int(list(str(num))[-nth])
        else:
            return -1
    except:
        return 0
