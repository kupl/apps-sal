def next_day_of_week(current_day, available_week_days):
    b = f"{available_week_days:07b}"[::-1]
    return b.find("1", current_day) + 1 or b.index("1") + 1
