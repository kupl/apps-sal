def next_day_of_week(current_day, available_week_days):
    return (f"{available_week_days:07b}"[::-1]*2).index('1',current_day)%7+1
