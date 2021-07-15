def find_digit(num, nth):
    try:
        return -1 if nth<1 else int(str(abs(num))[::-1][nth-1])
    except:
        return 0
