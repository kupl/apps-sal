from operator import add, sub, mul, truediv, floordiv

div = truediv #floordiv

arithmetic = lambda a, b, s: eval(s[:3])(a, b)
