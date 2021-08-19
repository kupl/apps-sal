def check_availability(sh, ct):
    return next((j for (i, j) in sh if ct > i and ct < j), 1)
