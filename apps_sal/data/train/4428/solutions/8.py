def sort_by_bit(arr):
    return sorted(arr, key=lambda x: (count(x), x))


def count(n):
    return bin(n)[2:].count("1")
