def sort_by_bit(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
