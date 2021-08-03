from datetime import datetime
from itertools import product

FORMATS = ["%Y-%m-%d", "%Y-%d-%m"]


def check_dates(records):
    correct = 0
    recoverable = 0
    uncertain = 0
    for start, end in records:
        good = set()
        right = False
        for i, (start_format, end_format) in enumerate(product(FORMATS, FORMATS)):
            try:
                start_date = datetime.strptime(start, start_format)
                end_date = datetime.strptime(end, end_format)
                if end_date >= start_date:
                    good.add((start_date, end_date))
                    if i == 0:
                        right = True
            except ValueError as e:
                pass
        if len(good) > 1:
            uncertain += 1
        elif len(good) == 1:
            if right:
                correct += 1
            else:
                recoverable += 1
    return [correct, recoverable, uncertain]
