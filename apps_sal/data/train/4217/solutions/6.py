from datetime import date

MONTHS_31 = (1,3,5,7,8,10,12)

def solve(a,b):
    cnt, first, last = 0, None, None
    for y in range(a,b+1):
        for m in MONTHS_31:
            d = date(y,m,1)
            if d.weekday()==4:
                cnt, first, last = cnt+1, first or d, d
    return first.strftime('%b'), last.strftime('%b'), cnt
