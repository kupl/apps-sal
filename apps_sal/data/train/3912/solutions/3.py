def arr2bin(arr):
    if all(map(lambda x: type(x) == int, arr)):
        return '{0:b}'.format(sum(arr))
    return False
