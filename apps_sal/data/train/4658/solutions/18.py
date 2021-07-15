max_product=lambda a,n:__import__("functools").reduce(lambda x, y: x * y, sorted(a)[-n:])
