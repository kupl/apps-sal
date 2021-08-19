def find_digit(num, nth):
    if nth < 0:
        return -1
    elif nth == 0:
        return -1
    try:
        k = nth
        i = str(num)
        final = i[-k]
        m = int(final)
        return m
    except:
        return 0
