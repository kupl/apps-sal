def past(h, m, s):
    totalMin = h * 60 + m
    totalSec = totalMin * 60 + s
    return totalSec * 1000
