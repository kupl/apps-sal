import re


def memesorting(s):

    def f(w):
        return re.search('{}'.format('.*?'.join(w)), s, re.IGNORECASE)
    a = [[m.span()[1], i] for (i, m) in enumerate((f(x) for x in ['bug', 'boom', 'edits'])) if m]
    return ['Roma', 'Maxim', 'Danik'][min(a)[1]] if a else 'Vlad'
