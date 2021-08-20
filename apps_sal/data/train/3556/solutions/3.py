def do(a, b, c, d, s):
    dc = {a: 0, b: 0}
    for i in s:
        if i in c:
            dc[[a, b][i in d]] += [1, 2][i.isupper()]
    return dc


def diamonds_and_toads(s, f):
    return do(*[['ruby', 'crystal', 'rcRC', 'cC', s], ['python', 'squirrel', 'psPS', 'sS', s]][f == 'evil'])
