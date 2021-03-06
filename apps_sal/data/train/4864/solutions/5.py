import re


def remove(s):
    li = []
    for i in s.split():
        start = re.search('^!+', i)
        end = re.search('!+$', i)
        i = re.sub('^!+', '', re.sub('!+$', '', i))
        m = min([len(start.group()) if start else 0, len(end.group()) if end else 0])
        li.append('!' * m + i + '!' * m)
    return ' '.join(li)
