def arr2bin(arr):
    return False if any((type(e) != int for e in arr)) else bin(sum(arr))[2:]
