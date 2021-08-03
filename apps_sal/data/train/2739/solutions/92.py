def cube_odd(lst): return None if not all(type(x) is int for x in lst) else sum(n ** 3 for n in lst if n & 1)
