climbing_grades = "VB V0 V0+".split() + ["V{}".format(i) for i in range(1, 18)]

def sort_grades(lst):
    return sorted(lst, key=climbing_grades.index)
