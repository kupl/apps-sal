def is_divide_by(n, a, b): return all(not n % x for x in (a, b)) if a and b else "ZeroDivisionError!"
