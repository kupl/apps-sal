def year_days(year):
    res = ""
    res += str(year)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                res += " has 366 days"
                return res
            else:
                res += " has 365 days"
                return res
        res += " has 366 days"
    else:
        res += " has 365 days"
    return res
