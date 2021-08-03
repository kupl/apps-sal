def find_digit(num, nth):

    try:
        return -1 if nth < 1 else int(str(num)[-nth])
    except:
        return 0
