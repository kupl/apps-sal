def distance(p, q): return -(not 0 < len(p) == len(q) > 0) or sum((x - y)**2for x, y in zip(p, q))**.5
