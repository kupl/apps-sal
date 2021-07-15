cube_odd = lambda lst: None if not all(type(x) is int for x in lst) else sum(n ** 3 for n in lst if n & 1)
