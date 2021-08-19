from datetime import date


def unlucky_days(year):
    contador = 0
    for i in range(1, 13):
        dato = date(year, i, 13)
        if dato.weekday() == 4:
            contador += 1
    return contador
