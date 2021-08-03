def is_inertial(array):
    if not array:
        return False
    max_value = max(array)
    if max_value % 2:
        return False
    try:
        return min(odd for odd in array if odd % 2) > max(even for even in array if even < max_value and even % 2 == 0)
    except ValueError:
        return False
