import calendar
c = calendar.Calendar()


def unlucky_days(year):
    cont = 0
    for mes in range(1, 13):
        for i in c.monthdayscalendar(year, mes):
            if i[4] == 13:
                cont = cont + 1
    return cont
