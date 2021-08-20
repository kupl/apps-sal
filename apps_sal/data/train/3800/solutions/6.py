import re
from string import ascii_uppercase as upper


def spreadsheet(s):
    x = re.search('^([A-Z]+)(\\d+)$', s)
    if x:
        (c, r) = x.groups()
        return f'R{r}C{sum(((upper.index(j) + 1) * 26 ** (len(c) - i - 1) for (i, j) in enumerate(c)))}'
    else:
        (r, c) = re.search('(?:R)(\\d+)(?:C)(\\d+)', s).groups()
        (s, c) = ([], int(c))
        if c == 26:
            return 'Z' + r
        while c > 1:
            (c, m) = divmod(c, 26)
            s.append([c, m])
        return ['', 'A'][c] + ''.join([upper[s[i][1] - ([2, 1][bool(s[i - 1][1])] if i > 0 else 1)] for i in range(len(s))])[::-1] + r
