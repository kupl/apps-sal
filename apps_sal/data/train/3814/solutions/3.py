def get_military_time(time):
    h = int(time[:2])
    if time.endswith("AM"):
        h = h % 12
    elif h < 12:
        h += 12
    return f"{h:02d}{time[2:8]}"
