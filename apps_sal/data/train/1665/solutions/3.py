def islist(A):
    return isinstance(A, list)
def same_structure_as(original,other):
    if islist(original) != islist(other):
        return False
    elif islist(original):
        if len(original) != len(other):
            return False
        for i in range(len(original)):
            if not same_structure_as(original[i], other[i]):
                return False
        return True
    else:
        return True
