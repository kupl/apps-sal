def next_day_of_week(c, a):
    return next((weekday - 1) % 7 + 1 for weekday in range(c+1, c+8) if (1 << ((weekday-1) % 7)) & a)
