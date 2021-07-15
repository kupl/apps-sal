def arr2bin(arr):
    return all(isinstance(n, int) and not isinstance(n, bool) for n in arr) and bin(sum(n for n in arr))[2:]
