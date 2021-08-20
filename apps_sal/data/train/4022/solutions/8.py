import re


def soundex(s):
    (d, li) = ({k: i for (i, j) in zip(list(range(1, 7)), ['bfpv', 'cgjkqsxz', 'dt', 'l', 'mn', 'r']) for k in j}, [])
    for i in s.split():
        first = i[0].upper()
        i = re.sub('(\\d)(\\1+)', '\\1', re.sub('[^aeiouy]', lambda x: str(d.get(x.group().lower(), x.group())), first + re.sub('[hwHW]', '', i[1:])))
        i = i[0] + re.sub('[aeiouyAEIOUY]', '', i[1:])
        li.append(first + f'{i[1:]:<03}'[:3])
    return ' '.join(li)
