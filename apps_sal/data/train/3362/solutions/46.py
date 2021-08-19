def sum_mix(arr):
    return sum((int(n) if type(n) == str else n for n in arr))
