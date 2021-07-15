from datetime import date

def solve(a, b):
    first = None
    count = 0
    for year in range(a, b + 1):
        for month in (1, 3, 5, 7, 8, 10, 12):
            d = date(year, month, 1)
            if d.weekday() == 4:
                last = d.strftime("%b")
                if first is None:
                    first = last
                count += 1
    return (first, last, count)

