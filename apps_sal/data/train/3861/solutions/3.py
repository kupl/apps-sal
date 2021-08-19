from re import findall
from itertools import groupby


def fire_and_fury(tweet):
    (s, match) = ([], findall('FIRE|FURY', tweet))
    if not match or not all([x in ['E', 'F', 'I', 'R', 'U', 'Y'] for x in tweet]):
        return 'Fake tweet.'
    for i in groupby(match):
        s.append((i[0], len(list(i[1]))))
    s = translated(s)
    return ' '.join(s)


def translated(s):
    string = []
    for i in s:
        if i[0] == 'FIRE':
            string.append('You ' + 'and you ' * (i[1] - 1) + 'are fired!')
        elif i[0] == 'FURY':
            string.append('I am ' + 'really ' * (i[1] - 1) + 'furious.')
    return string
