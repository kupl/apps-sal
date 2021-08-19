def find_digit(num, nth):
    # if nth is <= 0
    if nth <= 0:
        # return -1
        return -1
    # convert the num to a string
    num = str(num)
    # find the index moving right to left
    index = len(num) - nth
    if index >= 0:
        # return number at that index
        return int(num[index])
    else:
        return 0
