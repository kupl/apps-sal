def leap(year):
    solu = True
    if year >= 1000:
        if year % 4 == 0:
            solu = True
            if year % 100 == 0:
                if year % 400 == 0:
                    solu = True
                else:
                    solu = False
        else:
            solu = False
    elif year >= 100:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    solu = True
                else:
                    solu = False
        else:
            solu = False
    else:
        if year % 4 == 0:
            solu = True
        else:
            solu = False

    return solu


def year_days(year):
    temp = year
    if temp == 0:
        return str(year) + " has 366 days"
    else:
        if temp < 0:
            temp *= -1

    if leap(temp):
        return str(year) + " has 366 days"
    else:
        return str(year) + " has 365 days"
