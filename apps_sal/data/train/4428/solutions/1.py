def sort_by_bit(a):
    return sorted(a, key=lambda x: (bin(x).count('1'), x))
