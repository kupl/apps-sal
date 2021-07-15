def sort_grades(lst):
    grades = ['VB', 'V0', 'V0+'] + ['V' + str(i) for i in range(1, 18)]
    return [i for i in grades if i in lst]
