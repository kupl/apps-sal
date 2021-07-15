from datetime import datetime

def unlucky_days(year):
    bfriday = 0
    for i in range(1, 13):
        if datetime(year, i, 13).strftime("%a") == "Fri":
            bfriday+=1
    return bfriday
