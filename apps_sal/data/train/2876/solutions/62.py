def check(a, x):
    [head, *tail] = a
    return True if head == x else False if len(tail) == 0 else check(tail, x)
