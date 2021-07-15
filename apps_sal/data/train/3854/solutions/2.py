from itertools import product

def check_dates(records):
    correct, recoverable, uncertain = 0, 0, 0
    for begin, end in records:
        parsings = [(d1,d2) for d1,d2 in product(parse(begin), parse(end)) if d1 <= d2]
        if len(parsings) != 1: uncertain += 1
        elif parsings[0] == (begin,end): correct += 1
        else: recoverable += 1
    return [correct, recoverable, uncertain]

def parse(date):
    y,m,d = date.split("-")
    if d <= "12" and m != d: yield "-".join([y,d,m])
    if m <= "12": yield date
