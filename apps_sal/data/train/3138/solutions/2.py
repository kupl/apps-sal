def climb(n):
    result = [1]
    for x in "{:b}".format(n)[1:]:
        result.append(result[-1]*2 + (x=='1'))
    return result
