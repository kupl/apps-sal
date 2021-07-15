def find_digit(num, nth):
    try:
        return int(str(num)[-nth]) if nth > 0 else -1
    except:
        return 0
