def feast(a, b):
    return 2 == (lambda a, b, z, j: (lambda f, arg: sum([f(*a) for a in arg]))(lambda a, b: a == b, [[a[j], b[j]], [a[z], b[z]]]))(a, b, (lambda: 777).__code__.co_nlocals, -(lambda _: 777).__code__.co_nlocals)
