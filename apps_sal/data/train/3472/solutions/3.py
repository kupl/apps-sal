def next_day_of_week(a, b):
    return (f"{b:7b}"[::-1] * 2).index("1", a) % 7 + 1
