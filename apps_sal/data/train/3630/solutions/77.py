# No if statements :-)
arithmetic = lambda a, b, o: getattr(__import__("operator"), o == 'divide' and 'itruediv' or o[:3])(a, b)
