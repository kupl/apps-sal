def check(a, x): return False if len(a) == 0 else True if a.pop() == x else check(a, x)
