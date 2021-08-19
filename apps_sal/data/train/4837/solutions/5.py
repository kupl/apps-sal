from re import sub


def parse(crontab):

    ranges = {
        0: ['minute', list(range(60))],
        1: ['hour', list(range(24))],
        2: ['day of month', list(range(1, 32))],
        3: ['month', list(range(1, 13))],
        4: ['day of week', list(range(7))]
    }
    trans = {
        3: '# JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC'.split(' '),
        4: 'SUN MON TUE WED THU FRI SAT SUN'.split(' ')
    }

    tabs = crontab.split(' ')
    res = []

    for i, tab in enumerate(tabs):

        lb, lst = ranges[i]
        tokens = tab.split(',')

        local = []
        for s in tokens:
            if sub(r'[^A-Z]', '', s):
                t_arr = trans[i]
                for t in t_arr:
                    if t in s:
                        s = s.replace(t, str(t_arr.index(t)))

            local += choose(lst, s)

        res.append('{}{}'.format(lb.ljust(15), ' '.join(str(v) for v in sorted(local))))

    return '\n'.join(res)


def choose(lst, s):
    res = []

    if s == '*':
        return lst
    if s.isdigit():
        return [i for i in lst if int(s) == i]

    if '-' in s and '/' not in s:
        s, e = [int(v) for v in s.split('-')]
        return [v for v in lst if s <= v <= e]

    if '/' in s:
        cr, step = s.split('/')
        step = int(step)
        return choose(lst, cr)[0::step]

    return []
