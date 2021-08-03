D = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12,
     'SUN': 0, 'MON': 1, 'TUE': 2, 'WED': 3, 'THU': 4, 'FRI': 5, 'SAT': 6}


def read(s, mini, maxi):
    res = set()
    for x in s.split(','):
        y = x.split('/')
        a, n = y if len(y) == 2 else (x, '1')
        z = a.split('-')
        b, c = z if len(z) == 2 else (mini, maxi) if a == '*' else (a, a)
        res.update(range(D[b] if b in D else int(b), (D[c] if c in D else int(c)) + 1, int(n)))
    return ' '.join(map(str, sorted(res)))


def parse(crontab):
    res, L = [], crontab.split()
    res.append(f"minute         {read(L[0], 0, 59)}")
    res.append(f"hour           {read(L[1], 0, 23)}")
    res.append(f"day of month   {read(L[2], 1, 31)}")
    res.append(f"month          {read(L[3], 1, 12)}")
    res.append(f"day of week    {read(L[4], 0, 6)}")
    return '\n'.join(res)
