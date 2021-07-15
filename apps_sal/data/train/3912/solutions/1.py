def arr2bin(arr):
    return all(type(n) == int for n in arr) and format(sum(arr), 'b')
