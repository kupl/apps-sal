calculate = lambda a, o, b, m=__import__("operator"): None if o not in "+-*/" or o == '/' and not b else {"+": m.__add__, "-": m.__sub__, "*": m.__mul__, "/": m.__truediv__}[o](a, b)
