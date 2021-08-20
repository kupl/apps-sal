import re


def pete_talk(s, a=None):
    a = {x.lower() for x in a or []}

    def f(x):
        x = x[0]
        return x if x.lower() in a else x[0] + '*' * (len(x) - 2) + x[-1] * (len(x) > 1)
    return ''.join((x.capitalize() for x in re.split('([!?.] ?)', re.sub('\\w+', f, s))))
