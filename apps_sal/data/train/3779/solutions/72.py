def past(h, m, s):
    min = h * 60 + m
    sec = min * 60 + s
    sumMilli = sec * 1000 
    return sumMilli
