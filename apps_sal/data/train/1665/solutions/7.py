def make_hash(nest):
    if isinstance(nest, list):
        elems = ''
        for elem in nest:
            elems += make_hash(elem)
        return '[' + elems + ']'
    else:
        return '*'

def same_structure_as(original,other):
    if make_hash(original) == make_hash(other):
        return True
    else:
        return False
