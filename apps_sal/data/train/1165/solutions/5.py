from datetime import date
from dateutil.relativedelta import relativedelta
cal = ["january", "february", "march",
       "april",
       "may",
       "june",
       "july",
       "august",
       "september",
       "october",
       "november",
       "december"]


def fun(i):
    for j in range(12):
        if(cal[j] == i):
            return j + 1


def fun1(i):
    return cal[i - 1]


for _ in range(int(input())):
    t, s = input().split()
    t = int(t)
    x = fun(s)
    if(x >= 7):
        s = date(2012, x, t) - relativedelta(days=+183)
    else:
        s = date(2012, x, t) + relativedelta(days=+183)
    y = fun1(s.month)
    print(s.day, y)
