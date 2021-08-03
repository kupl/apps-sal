def sort_by_bit(arr):
    return sorted(arr, key=lambda x: (str('{:032b}'.format(x)).count('1'), x))
