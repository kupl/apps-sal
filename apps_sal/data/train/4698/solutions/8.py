def is_int_array(a): return isinstance(a, list) and all(isinstance(i, (int, float)) and i == int(i) for i in a)
