def closest(lst):
    m = min(lst, key=lambda x: abs(0 - x))
    return m if [abs(v) for v in set(lst)].count(abs(m)) == 1 else None
