def sort_number(a):
    a = sorted(a)
    a[-1] = 2 if a[-1] == 1 else 1
    return sorted(a)
