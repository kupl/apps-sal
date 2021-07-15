def invert(lst):
    result = []
    for num in lst:
        if num < 0:
            result.append(abs(num))
        elif num > 0:
            result.append(num - num * 2)
        else:
            result.append(0)
    return result
