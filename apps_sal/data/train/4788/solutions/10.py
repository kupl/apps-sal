def sort_grades(l):
    return sorted(l, key=lambda g: float(g[1:].replace('+', '.5').replace('B', '-1')))
