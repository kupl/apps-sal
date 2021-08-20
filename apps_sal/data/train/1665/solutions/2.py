def same_structure_as(a, b):
    return False if not (isinstance(a, list) and isinstance(b, list)) or len(a) != len(b) else all((same_structure_as(c, d) for (c, d) in zip(a, b) if isinstance(c, list)))
