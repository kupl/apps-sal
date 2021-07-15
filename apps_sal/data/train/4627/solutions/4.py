def closest(lst):
    lst = sorted(set(lst), key=abs)
    if len(lst) > 1 and abs(lst[0]) == abs(lst[1]):
        return None
    return lst[0]
