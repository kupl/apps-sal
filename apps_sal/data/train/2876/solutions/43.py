check = lambda a,x: False if len(a) == 0 else True if a.pop() == x else check(a,x)
