def closest(lst):
    m = min(lst, key=lambda x: abs(x))
    if not m or -m not in lst: return m
