combine = lambda *args: [el[0] for el in args] + combine(*[el[1:] for el in args if len(el) > 1]) if args else []
