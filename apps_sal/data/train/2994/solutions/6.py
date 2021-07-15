def find_digit(num, nth):
    try:
        return int(str(abs(num))[-nth]) if nth > 0 else -1
    except:
        return 0
