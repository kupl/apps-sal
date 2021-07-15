def find_missing_number(sequence):
    sequence=sequence.rsplit(sep=' ')
    if sequence==['']:
        return 0
    for a in sequence:
        try: int(a)
        except ValueError:    
            return 1
    sequence=[int(b) for b in sequence]
    for c in range(1,max(sequence)+1):
        if c not in sequence:
            return c
    else:
        return 0
