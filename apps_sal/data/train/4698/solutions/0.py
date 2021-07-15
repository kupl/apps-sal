def is_int_array(a):
    return isinstance(a, list) and all(isinstance(x, (int, float)) and x == int(x) for x in a)
