def dating_range(x): return '%s-%s' % (str(int(x - 0.1 * x)), str(int(x + 0.1 * x))) if x <= 14 else '%s-%s' % (str(int(x / 2 + 7)), str(int(x - 7) * 2))
