def unlucky_days(year):
    from datetime import date
    black_Fri = 0
    for i in range(1,13):
        if date(year, i, 13).weekday() == 4:
            black_Fri += 1
    return black_Fri
