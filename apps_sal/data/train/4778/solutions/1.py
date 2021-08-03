def money(student): return 5 * student.fives + 10 * student.tens + 20 * student.twenties


def most_money(students):
    if len(students) == 1:
        return students[0].name
    D = {money(student): student.name for student in students}
    return "all" if len(D) == 1 else D[max(D)]
