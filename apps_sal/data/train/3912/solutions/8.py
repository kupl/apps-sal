def arr2bin(arr):
    if all((type(x) is int for x in arr)):
        return '{:b}'.format(sum(arr))
    else:
        return False
