
def canonize(s):
    return s.lower().translate(str.maketrans('àéïô','aeio'))

def could_be(original, another):
    if not original or not another:
        return False
    
    original = [canonize(o) for o in original.translate(str.maketrans("!,;:?.","      ")).split()]
    another  = [canonize(a) for a in another.translate(str.maketrans("!,;:?.","      ")).split()]
    if not original or not another:
        return False
    
    return all(a in original for a in another)
