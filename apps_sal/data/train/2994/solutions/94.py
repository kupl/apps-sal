
def find_digit(num, nth):
    y = list(str(num))
    if nth > len(y):
        return 0
    if nth <= 0:
        return -1
    else:
        return int(str(num)[-nth])
