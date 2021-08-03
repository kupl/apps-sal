import re


def soundex(s):
    d, li = {k: i for i, j in zip(list(range(1, 7)), ['bfpv', 'cgjkqsxz', 'dt', 'l', 'mn', 'r'])for k in j}, []
    for i in s.split():
        first = i[0].upper()
        i = re.sub(r'(\d)(\1+)', r'\1', re.sub(r'[^aeiouy]', lambda x: str(d.get(x.group().lower(), x.group())), first + re.sub(r'[hwHW]', '', i[1:])))
        i = i[0] + re.sub(r'[aeiouyAEIOUY]', '', i[1:])
        li.append(first + (f"{i[1:]:<03}")[:3])
    return " ".join(li)
