def sort_grades(lst):
    grades = ['VB', 'V0', 'V0+']
    for i in range(1, 18):
        grades.append('V' + str(i))
    return sorted(lst, key=grades.index)
