from bisect import bisect_left as bisect
from datetime import date

CONFIG = [
    ("Capricorn",   19),
    ("Aquarius",    18),
    ("Pisces",      20),
    ("Aries",       19),
    ("Taurus",      20),
    ("Gemini",      20),
    ("Cancer",      22),
    ("Leo",         22),
    ("Virgo",       22),
    ("Libra",       22),
    ("Scorpio",     21),
    ("Sagittarius", 21),
    ("Capricorn",   31)]

DATES, _SIGNS = map(tuple, zip(*((date(1992, min(i,12), d), s) for i,(s,d) in enumerate(CONFIG,1))))

def get_zodiac_sign(d, m):
    return _SIGNS[bisect(DATES, date(1992,m,d))]
