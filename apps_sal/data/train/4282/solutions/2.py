import re


def hungry_seven(arr):
    return (lambda h: lambda x: h(h, x))(lambda h, x: h(h, re.sub('(7+)(89)', '\\2\\1', x)) if re.search('(7+)(89)', x) else [int(c) for c in x])(''.join(map(str, arr)))
