from functools import reduce
from collections import defaultdict
import re
FINDER = re.compile('(.+?)\\s+(\\d+)%')
SPLITTER = re.compile('\\s|-')


def create_report(names):
    dct = defaultdict(int)
    for (what, n) in FINDER.findall('%'.join(names) + '%'):
        if what == 'Labrador Duck':
            return ['Disqualified data']
        lst = SPLITTER.split(what)
        key = ''.join((word[:6 // len(lst) + (len(lst) == 4 and i >= 2)] for (i, word) in enumerate(lst))).upper()
        dct[key] += int(n)
    lst = []
    for (k, n) in sorted(dct.items()):
        lst.extend([k, n])
    return lst
