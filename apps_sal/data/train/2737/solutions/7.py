import re
r = re.compile(r'(?<=\[)\[|(?<=\])\]')


def near_flatten(nested):
    return sorted(eval('[' + r.sub('', str(nested)) + ']'), key=lambda x: x[0])
