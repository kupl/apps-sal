def past(h, m, s):
    hour_minute = h*60
    minute_millisecond = m*60000
    second_millisecond = s*1000
    sum = (hour_minute*60000)+minute_millisecond+second_millisecond
    return sum
