from datetime import datetime as dt
from itertools import product, starmap
from collections import defaultdict


CORRECT, RECOVER, UNSURE = range(3)
TIMESTR_MODELS = ('%Y-%m-%d', '%Y-%d-%m')            # wanted, inverted


def check_dates(records):
    out = [0] * 3
    for r in records:
        out[check(*r)] += 1
    return out


def check(start, finish):
    cndsS, cndsF = getPossibleDates(start), getPossibleDates(finish)
    areOK = [i1 + i2 for(d1, i1), (d2, i2) in product(cndsS, cndsF) if d1 <= d2]

    return (UNSURE if len(areOK) > 1 else
            RECOVER if areOK[0] else
            CORRECT)


def getPossibleDates(s):
    cnds = defaultdict(lambda: 1)
    for i, model in enumerate(TIMESTR_MODELS):
        try:
            cnds[dt.strptime(s, model)] *= i
        except ValueError:
            pass
    return cnds.items()
