unlucky_days = lambda y: sum(__import__("datetime").date(y, m, 13).weekday() == 4 for m in range(1, 13))
