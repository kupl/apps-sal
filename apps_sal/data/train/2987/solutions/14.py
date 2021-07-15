is_divide_by = lambda n, a, b: all(not n % x for x in (a, b)) if a and b else "ZeroDivisionError!"
