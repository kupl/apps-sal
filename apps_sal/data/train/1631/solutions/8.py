snail = lambda a: list(a[0]) + snail(list(zip(*a[1:]))[::-1]) if a else []

