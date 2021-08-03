def arr2bin(arr):

    s = 0

    for x in arr:
        if type(x) is int:
            s += x
        else:
            return False

    return '{:b}'.format(s)
