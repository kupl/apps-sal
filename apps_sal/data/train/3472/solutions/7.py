def next_day_of_week(day, week):
    days = [d for d, v in enumerate(bin(week)[2:][::-1], 1) if int(v)]
    return next((d for d in days if d > day), days[0])
