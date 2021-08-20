def arr2bin(arr):
    if any((type(a) is not int for a in arr)):
        return False
    return bin(sum(arr))[2:]
