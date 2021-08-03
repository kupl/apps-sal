def sort_grades(gs):
    return sorted(gs, key=grade)


def grade(v):
    if v == 'VB':
        return -2
    if v == 'V0':
        return -1
    if v == 'V0+':
        return 0
    return int(v[1:])
