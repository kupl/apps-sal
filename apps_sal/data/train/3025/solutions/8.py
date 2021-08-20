locate = l = lambda a, x: any((l(e, x) if [] == e * 0 else e == x for e in a))
