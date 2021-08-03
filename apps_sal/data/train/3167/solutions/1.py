def twos_difference(lst):
    return [(num, num + 2) for num in sorted(lst) if num + 2 in lst]
