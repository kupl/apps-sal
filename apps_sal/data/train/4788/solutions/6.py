def sort_grades(lst):
    grades = ["VB","V0","V0+"]+["V{}".format(i) for i in range(1, 18)]
    return sorted(lst, key=lambda l: grades.index(l))
