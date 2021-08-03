import re

PATTERN = re.compile(r'(\d+) (\w+)')


def repl(m):
    n = int(m.group(1))
    return "{} {}{}{}".format(n,
                              'bu' if n == 2 else 'ga' if n > 9 else '',
                              m.group(2) if n < 2 else m.group(2)[:-1],
                              '' if n < 3 else 'zo' if n < 10 else 'ga')


def sursurungal(txt): return PATTERN.sub(repl, txt)
