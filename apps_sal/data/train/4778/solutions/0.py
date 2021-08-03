def most_money(students):
    total = []
    for student in students:
        total.append((student.fives * 5) + (student.tens * 10) + (student.twenties * 20))

    if min(total) == max(total) and len(students) > 1:
        return "all"
    else:
        return students[total.index(max(total))].name
