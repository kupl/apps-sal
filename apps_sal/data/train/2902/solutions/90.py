def opposite(number):
    if number >= 1:
        tempnum = number + number
        result = number - tempnum
        return result
    if number <= -1:
        tempnum = number + number
        result = number - tempnum
        return result
    else:
        return 0
