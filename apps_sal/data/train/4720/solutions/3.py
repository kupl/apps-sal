hyperrectangularity_properties = h = lambda a: () if [] != a * 0 else (lambda f, *s: None if f == None or s else (len(a),) + f)(*(set(map(h, a)) or {()}))
