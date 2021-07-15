def next_day_of_week(current_day, available_week_days):
    x = 2 ** current_day
    while not x & available_week_days:
        x = max(1, (x * 2) % 2 ** 7)
    return x.bit_length()
