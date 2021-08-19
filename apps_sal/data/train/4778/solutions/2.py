def most_money(students):
    BillGatesKid = students[0]
    NumOfStudents = len(students)
    if NumOfStudents == 1:
        return BillGatesKid.name
    for s in students:
        if s.fives * 5 + s.tens * 10 + s.twenties * 20 > BillGatesKid.fives * 5 + BillGatesKid.tens * 10 + BillGatesKid.twenties * 20:
            BillGatesKid = s
        elif s.fives * 5 + s.tens * 10 + s.twenties * 20 == BillGatesKid.fives * 5 + BillGatesKid.tens * 10 + BillGatesKid.twenties * 20:
            NumOfStudents -= 1
            if NumOfStudents == 0:
                return 'all'
    return BillGatesKid.name
