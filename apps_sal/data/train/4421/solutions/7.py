def to_seconds(time):
    try:
        (h, m, s) = map(int, time.split(':'))
        if not (len(time) == 8 and 0 <= m < 60 > s >= 0):
            return None
    except ValueError:
        return None
    return h * 3600 + m * 60 + s
