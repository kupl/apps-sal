from itertools import chain
import re

MONTHS_DAYS = list(map(str.split, ('JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC', 'SUN MON TUE WED THU FRI SAT')))
REPL_NAMES = {s: str(i) for i, s in chain(*(enumerate(lst, detla) for lst, detla in zip(MONTHS_DAYS, (1, 0))))}
RANGES = (('minute', 0, 59), ('hour', 0, 23), ('day of month', 1, 31), ('month', 1, 12), ('day of week', 0, 6))


def parse(s):
    s = re.sub(r'[A-Z]+', lambda m: REPL_NAMES[m[0]], s)
    return '\n'.join(parsePart(part, name, (a, b)) for part, (name, a, b) in zip(s.split(), RANGES))


def parsePart(part, name, rng):
    out = []
    for s in part.split(','):
        i, j = list(map(s.find, '-/'))
        step, j = (1, len(s)) if j == -1 else (int(s[j + 1:]), j)
        start, end = rng if s[0] == '*' else (int(s),) * 2 if i == -1 else list(map(int, (s[:i], s[i + 1:j])))
        out.extend(list(range(start, end + 1, step)))

    return f"{name:15}{ ' '.join(map(str, sorted(out))) }"
