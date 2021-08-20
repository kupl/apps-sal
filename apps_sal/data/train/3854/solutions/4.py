from datetime import date
from itertools import product


def check_dates(records):
    (correct, recoverable, uncertain) = (0, 0, 0)

    def parse(s):
        return date(*[int(d) for d in s.split('-')])
    for date_pair in records:
        (start_date, end_date) = map(parse, date_pair)
        orig_duration_valid = (end_date - start_date).days >= 0
        poss_start_dates = set([start_date] + ([date(start_date.year, start_date.day, start_date.month)] if start_date.day <= 12 else []))
        poss_end_dates = set([end_date] + ([date(end_date.year, end_date.day, end_date.month)] if end_date.day <= 12 else []))
        only_one_possible = sum(((poss_end - poss_start).days >= 0 for (poss_start, poss_end) in product(poss_start_dates, poss_end_dates))) == 1
        if orig_duration_valid and only_one_possible:
            correct += 1
        elif only_one_possible:
            recoverable += 1
        else:
            uncertain += 1
    return [correct, recoverable, uncertain]
