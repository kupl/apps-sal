def move_zeros(array):
    return [a for a in array if isinstance(a, bool) or a != 0] + [a for a in array if not isinstance(a, bool) and a == 0]
