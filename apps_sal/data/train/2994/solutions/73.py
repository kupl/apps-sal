def find_digit(num, nth):
    if nth < 1:
        return -1
    else:
        try:
            number = int(str(num)[-nth])
        except:
            number = 0
        return number
