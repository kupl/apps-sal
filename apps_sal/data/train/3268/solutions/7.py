words_to_object = lambda s: "[" + ", ".join("{name : '%s', id : '%s'}" % t for t in zip(*[iter(s.split())]*2)) + "]"
