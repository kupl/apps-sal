def past(h, m, s):
    hour_mm = h*60*60*1000
    minute_mm = m*60*1000
    seconds_mm = s*1000
    
    return hour_mm + minute_mm + seconds_mm
