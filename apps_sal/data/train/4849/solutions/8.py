from re import escape, split as my_split


def my_very_own_split(string, delimiter=None):
    if delimiter == '':
        raise None
    for s in my_split(r'{0}'.format(escape(delimiter) if delimiter else '[\s\t$]+'), string):
        yield s
