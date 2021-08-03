def distinct_digit_year(y): return next(i for i in range(y + 1, 9000)if len(set(str(i))) == 4)
