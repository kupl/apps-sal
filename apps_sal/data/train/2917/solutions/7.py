distinct_digit_year=lambda y:next(i for i in range(y+1,9000)if len(set(str(i)))==4)
