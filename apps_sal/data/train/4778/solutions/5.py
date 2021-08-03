def cashmuny(student):
    return student.fives * 5 + student.tens * 10 + student.twenties * 20


def most_money(students):
    timdeo = students[0]
    all = False
    if len(students) == 1:
        return timdeo.name
    for s in students[1:]:
        if cashmuny(s) > cashmuny(timdeo):
            timdeo = s
            all = False
        elif cashmuny(s) == cashmuny(timdeo):
            all = True
    if all == False:
        return timdeo.name
    if all == True:
        return "all"
