def sum_digits(number):
    absNum = number if number > 0 else -number
    strList = list(str(absNum))
    return sum(map(lambda x: int(x), strList))
