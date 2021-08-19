def sort_by_bit(arr):
    return sorted(arr, key=lambda n: (bin(n).count('1'), n))
