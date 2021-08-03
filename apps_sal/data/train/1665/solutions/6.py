def same_structure_as(a, b):
    def structure(arr): return [0 if type(e) != list else structure(e) for e in arr]
    return type(a) == type(b) and structure(a) == structure(b)
