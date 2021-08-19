def next_day_of_week(current_day, available_week_days):
    # coding and coding..
    d = {1: 1, 2: 2, 3: 4, 4: 8, 5: 16, 6: 32, 7: 64}

    while True:
        if current_day == 7:
            current_day = 0
        current_day += 1

        if available_week_days & d[current_day]:
            return current_day
