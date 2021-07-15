unique_digit_products = lambda a, r=__import__("functools").reduce: len({r(int.__mul__, map(int, str(e))) for e in a})
