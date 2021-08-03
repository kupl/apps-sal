lcs = (lambda y: y(y))(lambda lcs: lambda x, y: '' if not x or not y else lcs(lcs)(x[:-1], y[:-1]) + x[-1] if x[-1] == y[-1] else max(lcs(lcs)(x[:-1], y), lcs(lcs)(x, y[:-1]), key=len))
