def closest(lst):
    result = min(lst, key=abs)
    return result if not result or -result not in lst else None
