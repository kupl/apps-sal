def find_digit(num, nth):
    if nth < 1:
        return -1
    if num < 0:
        num *= -1
    num = str(num)
    if nth > len(num):
        return 0
    return int(num[len(num) - nth])
