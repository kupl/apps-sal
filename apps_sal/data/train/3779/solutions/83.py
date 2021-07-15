def past(h, m, s):
    new_hour = h * 3600000
    new_minute = m * 60000
    new_second = s * 1000
    total_time = new_hour + new_minute + new_second
    return total_time
