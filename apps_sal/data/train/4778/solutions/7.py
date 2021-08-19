def most_money(students):

    def money(s):
        return s.fives * 5 + s.tens * 10 + s.twenties * 20
    students = sorted(students, key=money, reverse=True)
    if len(students) != 1 and money(students[0]) == money(students[1]):
        return 'all'
    return students[0].name
