def sort_grades(lst):
    return sorted(lst, key=lambda s: float(s[1:].replace('B', '-1').replace('+', '.5')))
