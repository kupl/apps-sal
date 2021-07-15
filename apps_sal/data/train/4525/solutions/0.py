import calendar

M = {calendar.month_name[i]: i - 1 for i in range(1, 13)}


def check_challenge(pledged, current, month):
    if pledged == current:
        return "Challenge is completed."
    m = M[month]
    per_month, rest = divmod(pledged, 12)
    todo = per_month * m + (min(rest, m))
    delta = current - todo
    if delta == 0 or m == 0:
        return "You are on track."
    elif delta > 0:
        return f"You are {delta} ahead of schedule!"
    else:
        return f"You are {-delta} behind schedule."
