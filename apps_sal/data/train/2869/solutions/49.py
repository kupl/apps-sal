def distinct(seq):
    unique = []
    for s in seq:
        if s not in unique:
            unique.append(s)
            
    return unique
