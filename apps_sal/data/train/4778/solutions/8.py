def most_money(students):
    allsame = True
    max = 0
    for s in students:
        smoney = s.fives * 5 + s.tens * 10 + s.twenties * 20
        if max == 0:
            richest, max = s.name, smoney
        elif smoney != max:
            allsame = False

        if smoney > max:
            richest, max = s.name, smoney

    return "all" if allsame and len(students) > 1 else richest
