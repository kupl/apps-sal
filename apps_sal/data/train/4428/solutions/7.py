def sort_by_bit(arr):
    return sorted(sorted(arr), key=lambda i: bin(i)[2:].count('1'))
