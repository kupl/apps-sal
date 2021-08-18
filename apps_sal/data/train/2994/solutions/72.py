def find_digit(num, nth):
    if nth <= 0:
        return -1
    num = str(num)
    index = len(num) - nth
    if index >= 0:
        return int(num[index])
    else:
        return 0
