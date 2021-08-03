def find_digit(num, nth):
    # your code here
    if nth > len(str(abs(num))):
        return 0
    elif nth > 0 and abs(num) >= nth:
        y = str(abs(num))
        return int(y[-nth])
    return -1
