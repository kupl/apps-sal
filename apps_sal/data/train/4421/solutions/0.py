def to_seconds(time):
    try:
        (s, m, h) = (int(time[-2:]), int(time[3:5]), int(time[:2]))
        return s + m * 60 + h * 3600 if m < 60 and s < 60 and (len(time) == 8) else None
    except:
        return None
