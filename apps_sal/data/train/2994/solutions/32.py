def find_digit(num, nth):
    num = str(num)
    if nth < 1:
        return -1
    if nth > len(num):
        return 0
    i = [char for char in num]
    return int(i[-nth])
