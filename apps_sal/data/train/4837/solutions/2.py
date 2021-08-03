import re

D = {0: [0, 59], 1: [0, 23], 2: [1, 31], 3: [1, 12], 4: [0, 6]}
REGEXES = ['(\d+)-(\d+)', '(\d+)-(\d+)/(\d+)', '(\d+)']
FORMAT = '''\
minute         {}
hour           {}
day of month   {}
month          {}
day of week    {}\
'''
DAYS = 'SUN MON TUE WED THU FRI SAT'.split()
MONTHS = 'X JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DES'.split()


def parse(ct):
    ct = re.sub(r'{}'.format('|'.join(DAYS)), lambda x: str(DAYS.index(x.group())), ct)
    ct = re.sub(r'{}'.format('|'.join(MONTHS)), lambda x: str(MONTHS.index(x.group())), ct)
    ct = [re.sub(r'\*', lambda _:'-'.join([str(k) for k in D[i]]), j) for i, j in enumerate(ct.split())]
    parser = []
    for i, j in enumerate(ct):
        sep = []
        for k in j.split(','):
            a, b, c = [re.search('^' + r + '$', k) for r in '(\d+)-(\d+) (\d+)-(\d+)/(\d+) (\d+)'.split()]
            if c:
                sep.append(int(k))
            elif b:
                x, y, z = map(int, b.groups())
                sep.extend(list(range(x, y + 1, z)))
            elif a:
                x, y = map(int, a.groups())
                sep.extend(list(range(x, y + 1)))
        parser.append(' '.join([str(i) for i in sorted(sep)]))
    return FORMAT.format(*parser)
