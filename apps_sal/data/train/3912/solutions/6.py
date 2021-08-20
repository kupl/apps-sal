def arr2bin(arr):
    if any((type(x) != int for x in arr)):
        return False
    return bin(sum(arr))[2:]
