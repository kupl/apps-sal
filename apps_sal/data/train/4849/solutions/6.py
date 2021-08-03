import re


def my_very_own_split(string, delimiter=None):
    if delimiter == '':
        raise ValueError('empty separator')
    if delimiter == None:
        delimiter = re.compile(r'\s+')
    else:
        delimiter = re.compile(re.escape(delimiter))
    print(delimiter)

    start = 0
    for m in re.finditer(delimiter, string):
        yield string[start:m.start()]
        start = m.end()

    yield string[start:]
