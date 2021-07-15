def closest(lst):
    m = min(lst, key=abs)
    return m if m == 0 or -m not in lst else None
