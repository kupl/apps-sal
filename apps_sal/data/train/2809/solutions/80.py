def digitize(n):
    result = list((int(x) for x in str(n)))
    return result[::-1]
