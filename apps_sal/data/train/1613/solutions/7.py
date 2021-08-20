from re import escape, sub


def solution(s, markers):
    return s if not markers else sub('( *[{}].*)'.format(escape(''.join(markers))), '', s)
