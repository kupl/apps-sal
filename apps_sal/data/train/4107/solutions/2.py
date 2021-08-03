from datetime import date


def half_life(person1, person2):
    p1 = list(map(int, person1.split("-")))
    p1_date = date(p1[0], p1[1], p1[2])
    p2 = list(map(int, person2.split("-")))
    p2_date = date(p2[0], p2[1], p2[2])
    if p1[0] > p2[0]:
        diff = p1_date - p2_date
        b = p1_date + diff
        return str(b)
    else:
        diff = p2_date - p1_date
        a = p2_date + diff
        return str(a)
