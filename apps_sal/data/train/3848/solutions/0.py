from datetime import datetime
from itertools import permutations


def unique_date(*args):
    dates = set()
    for p in permutations(args):
        try:
            date = '{:02}/{:02}/{:02}'.format(*p)
            datetime.strptime(date, '%y/%m/%d')
            dates.add(date)
        except ValueError:
            pass
    return dates.pop() if len(dates) == 1 else "ambiguous" if dates else "invalid"
