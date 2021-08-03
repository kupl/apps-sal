solve = lambda a, b, c=__import__('collections').Counter: not c(b) - c(a) and len(a) - len(b)
