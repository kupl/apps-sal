def naughty_or_nice(data):
    nice = 0
    for month in data:
        for day in data[month]:
            nice += 1 if data[month][day] == "Nice" else -1
    return "Nice!" if nice >= 0 else "Naughty!"
