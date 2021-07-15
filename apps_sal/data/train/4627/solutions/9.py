def closest(lst):
    return min(lst, key= lambda x: abs(x)) if (-min(lst, key= lambda x: abs(x))) not in lst or min(lst, key= lambda x: abs(x)) == 0 else None
