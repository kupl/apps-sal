def lineup_students(string):
    students = string.split()
    students.sort()
    s = sorted(students, key=len)

    return s[::-1]
