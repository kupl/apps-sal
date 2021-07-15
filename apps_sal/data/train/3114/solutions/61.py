def year_days(y):
    return f"{y} has {366 if (not y%400) or ((y%100) and not y%4) else 365} days"
