past = lambda *args: __import__('functools').reduce(lambda a, b: a * 60 + b, args) * 1000
