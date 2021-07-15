s = same_structure_as = lambda a, b: type(a) == type(b) == list and len(a) == len(b) and all(map(s, a, b)) if type(a) == list else 1
