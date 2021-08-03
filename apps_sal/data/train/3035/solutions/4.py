def getMatrixProduct(a, b): return -((len(a) and len(a[0])) != len(b)) or [[sum(x * y for x, y in zip(r, c))for c in zip(*b)]for r in a]
